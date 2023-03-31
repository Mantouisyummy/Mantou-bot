from typing import Union

import lavalink
import asyncio
from disnake import TextChannel, Thread, InteractionResponded, ApplicationCommandInteraction, \
    MessageInteraction
from disnake.abc import GuildChannel
from disnake.ext import commands
from disnake.ext.commands import Cog, CommandInvokeError
from disnake.utils import get
from lavalink import TrackLoadFailedEvent, DefaultPlayer, PlayerUpdateEvent, TrackEndEvent, QueueEndEvent

from core.classes import Bot
from core.embeds import ErrorEmbed,InfoEmbed
from library.errors import MissingVoicePermissions, BotNotInVoice, UserNotInVoice, UserInDifferentChannel
from library.functions import update_display, ensure_voice, toggle_autoplay, get_recommended_track


class Events(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    async def cog_load(self):
        await self.bot.wait_until_ready()

        lavalink.add_event_hook(self.track_hook)

    async def track_hook(self, event):
        if isinstance(event, PlayerUpdateEvent):
            player: DefaultPlayer = event.player

            if event.player.fetch("autoplay") and len(event.player.queue) == 0:
                recommendation = await get_recommended_track(player, player.current)

                event.player.add(requester=0, track=recommendation)

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
    async def on_voice_state_update(self, member, before, after):
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

        voice_client = get(self.bot.voice_clients, guild=member.guild)
        try:
            voice_channel = get(member.guild.voice_channels,id=voice_client.channel.id)
        except AttributeError:
            await asyncio.sleep(1)
            voice_channel = get(member.guild.voice_channels,id=voice_client.channel.id)
            pass
        if (
                before.channel is not None
                and after.channel is None
                and member.id != self.bot.user.id
                and len(voice_channel.members) == 1
        ):
            timer = 0
            while timer < 120:
                if len(voice_channel.members) > 1:
                    return  # Cancel the process

                await asyncio.sleep(1)
                timer += 1

            player: DefaultPlayer = self.bot.lavalink.player_manager.get(member.guild.id)

            await player.stop()
            player.queue.clear()

            channel: Union[GuildChannel, TextChannel, Thread] = self.bot.get_channel(int(player.fetch("channel")))
            message = await channel.send(
                    embed=InfoEmbed("超過兩分鐘已沒人聽歌 我先跑路啦 👋"),
                )
            await voice_client.disconnect()
            try: 
                await update_display(self.bot, player, message,delay=3)
            except ValueError: # There's no message to update
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