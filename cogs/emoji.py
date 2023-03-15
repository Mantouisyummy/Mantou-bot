import disnake
from disnake.ext import commands
from disnake import ApplicationCommandInteraction,Option
from typing import Optional
import random

class Emoji(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        super().__init__()
    @commands.Cog.listener()
    async def on_ready(self):
        print("Emoji Ready!")

    @commands.slash_command(name="emoji", description="將Emoji變為圖片!",name_localizations={"zh-TW":"獲取表符"},guild_ids=[1003837176464810115])
    async def emoji(self, interaction: ApplicationCommandInteraction,emoji:str = Option(name="emoji",description="你要獲取圖片的表符")):
        await interaction.response.send_message("你家的表符為 {}".format(emoji),ephemeral=True)

        

def setup(bot):
    bot.add_cog(Emoji(bot))