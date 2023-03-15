import disnake
from disnake.ext import commands
from disnake import ApplicationCommandInteraction,Embed,Colour
import random
class View(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @disnake.ui.button(label="更新", style=disnake.ButtonStyle.green, emoji="<:robot:955475991109718016>")
    async def update(self, button: disnake.ui.Button, interaction: ApplicationCommandInteraction):
        await interaction.edit_original_message(embed=self)
        

class BotInfo(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        super().__init__()
    @commands.Cog.listener()
    async def on_ready(self):
        print("Botinfo Ready!")

    @commands.slash_command(name="botinfo", description="查看機器人的狀態")
    async def botinfo(self, interaction: ApplicationCommandInteraction):
        embed = Embed(title="",description="",colour=Colour.random())
        embed.add_field(name="伺服器",value=len(self.bot.guilds),inline=True)
        embed.add_field(name="成員",value="I dont know.",inline=True)
        embed.add_field(name="音樂",value="<:green_dot:1037366718592458853> 節點正常!",inline=False)
        embed.set_author(name=self.bot.user.name,icon_url=self.bot.user.avatar.url)
        embed.set_footer(text="此機器人使用了disnake烹調而成",icon_url="https://guide.disnake.dev/public/disnake-logo.png")
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(BotInfo(bot))