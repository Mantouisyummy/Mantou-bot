from typing import Union

import lavalink
import asyncio
from disnake import TextChannel, Thread, InteractionResponded, ApplicationCommandInteraction, \
    MessageInteraction,Member
from disnake.abc import GuildChannel
from disnake.ext import commands
from disnake.utils import get
from disnake.ext.commands import Cog, CommandInvokeError
from lavalink import TrackLoadFailedEvent, DefaultPlayer, PlayerUpdateEvent, TrackEndEvent, QueueEndEvent

from core.classes import Bot
from core.embeds import ErrorEmbed,InfoEmbed
from library.errors import MissingVoicePermissions, BotNotInVoice, UserNotInVoice, UserInDifferentChannel
from library.functions import update_display, ensure_voice, toggle_autoplay, get_recommended_tracks
from library.variables import Variables


class Events(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    async def cog_load(self):
        await self.bot.wait_until_ready()

        lavalink.add_event_hook(self.track_hook)
    
    async def sleep(self):
        await asyncio.sleep(120)
    
    async def track_hook(self, event):
        if isinstance(event, PlayerUpdateEvent):
            player: DefaultPlayer = event.player

            if event.player.fetch("autoplay") and len(event.player.queue) <= 10:
                recommendations = await get_recommended_tracks(
                    Variables.SPOTIFY_CLIENT, event.player, ([event.player.current] + event.player.queue)[-10:], 20
                )

                for track in recommendations:
                    event.player.add(requester=0, track=track)

            try:
                await update_display(self.bot, player)
            except ValueError:
                pass

        elif isinstance(event, TrackEndEvent):
            player: DefaultPlayer = event.player

            try:
                await update_display(self.bot, player)
            except ValueError:
                pass

        elif isinstance(event, QueueEndEvent):
            player: DefaultPlayer = event.player

            try:
                await update_display(self.bot, player)
            except ValueError:
                pass

        elif isinstance(event, TrackLoadFailedEvent):
            player: DefaultPlayer = event.player

            # noinspection PyTypeChecker
            channel: Union[GuildChannel, TextChannel, Thread] = self.bot.get_channel(int(player.fetch("channel")))

            message = await channel.send(
                embed=ErrorEmbed(f"無法播放歌曲: {event.track['title']}", f"原因: `{event.original or 'Unknown'}`")
            )

            await player.skip()

            await update_display(self.bot, player, message, delay=5)

    @commands.Cog.listener(name="on_slash_command_error")
    async def on_slash_command_error(self, interaction: ApplicationCommandInteraction, error: CommandInvokeError):
        if isinstance(error.original, MissingVoicePermissions):
            embed = ErrorEmbed("指令錯誤", "我需要 `連接` 和 `說話` 權限才能夠播放音樂")

        elif isinstance(error.original, BotNotInVoice):
            embed = ErrorEmbed("指令錯誤", "我沒有連接到一個語音頻道")

        elif isinstance(error.original, UserNotInVoice):
            embed = ErrorEmbed("指令錯誤", "你沒有連接到一個語音頻道")

        elif isinstance(error.original, UserInDifferentChannel):
            embed = ErrorEmbed("指令錯誤", f"你必須與我在同一個語音頻道 <#{error.original.voice.id}>")

        else:
            raise error.original

        try:
            await interaction.response.send_message(embed=embed)
        except InteractionResponded:
            await interaction.edit_original_response(embed=embed)

    @commands.Cog.listener(name="on_voice_state_update")
    async def on_voice_state_update(self, member:Member, before, after):
        if (
                before.channel is not None
                and after.channel is None
                and member.id == self.bot.user.id
        ):
            player: DefaultPlayer = self.bot.lavalink.player_manager.get(member.guild.id)

            await player.stop()
            player.queue.clear()

            try:
                await update_display(self.bot, player)
            except ValueError:  # There's no message to update
                pass
        
        try:
            voice_client = get(self.bot.voice_clients, guild=member.guild)
            voice_channel = get(member.guild.voice_channels,id=voice_client.channel.id)
            print(voice_client.channel.id)
            if after.channel is not None:
                # 獲取語音頻道中的成員列表
                members = after.channel.members
                # 如果語音頻道中只有一個成員，並且是機器人本身
                if len(members) == 1 and members[0] == self.bot.user:
                    # 創建一個異步任務來執行check_and_disconnect函數，並將其保存到bot的屬性中
                    task = asyncio.create_task(self.check_and_disconnect(after.channel))
                # 如果語音頻道中有多於一個成員，並且bot有一個正在執行的任務
                elif len(members) > 1 and hasattr(task, "task") and not task.done():
                    # 取消該任務
                    task.cancel()
                        
                task = asyncio.create_task(disconnect())
                try:
                    await asyncio.wait_for(task, timeout=120)
                except asyncio.TimeoutError:
                    task.cancel()
        except (UnboundLocalError,AttributeError):
            pass
    async def check_and_disconnect(self, channel):
        try:
            # 等待2分鐘
            await asyncio.sleep(120)
            # 如果語音頻道中仍然只有一個成員，並且是機器人本身
            if len(channel.members) == 1 and channel.members[0] == self.bot.user:
                # 斷開語音連接
                player: DefaultPlayer = self.bot.lavalink.player_manager.get(member.guild.id)

                channel: Union[GuildChannel, TextChannel, Thread] = self.bot.get_channel(int(player.fetch("channel")))

                guild = self.bot.get_guild(1003837176464810115)
                emoji = get(guild.emojis, id=1078318173616611378)

                message = await channel.send(
                    embed=InfoEmbed(f"超過兩分鐘已沒人聽歌 我先跑路啦 {emoji}"),
                )

                await voice_client.disconnect()

                try: 
                    await update_display(self.bot, player, message,delay=10)
                except ValueError: # There's no message to update
                    pass
                await player.stop()  
                player.queue.clear()
        except asyncio.CancelledError:
            # 如果任務被取消，則不執行任何操作
            pass

    @commands.Cog.listener(name="on_message_interaction")
    async def on_message_interaction(self, interaction: MessageInteraction):
        if interaction.data.custom_id.startswith("control"):
            if interaction.data.custom_id.startswith("control.empty"):
                await interaction.response.edit_message()

                return

            try:
                await ensure_voice(interaction, should_connect=False)
            except (UserNotInVoice, BotNotInVoice, MissingVoicePermissions, UserInDifferentChannel):
                return

            player: DefaultPlayer = self.bot.lavalink.player_manager.get(interaction.guild_id)

            match interaction.data.custom_id:
                case "control.resume":
                    await player.set_pause(False)

                case "control.pause":
                    await player.set_pause(True)

                case "control.stop":
                    await player.stop()
                    player.queue.clear()

                case "control.previous":
                    await player.seek(0)

                case "control.next":
                    await player.skip()

                case "control.shuffle":
                    player.set_shuffle(not player.shuffle)

                case "control.repeat":
                    player.set_loop(player.loop + 1 if player.loop < 2 else 0)

                case "control.rewind":
                    await player.seek(round(player.position) - 10000)

                case "control.forward":
                    await player.seek(round(player.position) + 10000)

                case "control.autoplay":
                    toggle_autoplay(player)

            await update_display(self.bot, player, interaction=interaction)


def setup(bot):
    bot.add_cog(Events(bot))