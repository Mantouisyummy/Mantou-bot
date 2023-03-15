import disnake
from disnake.ext import commands
from disnake import ApplicationCommandInteraction
import random
class View(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @disnake.ui.button(label="再骰一次", style=disnake.ButtonStyle.green, emoji="<:Update:1036992904352243743>")
    async def update(self, button: disnake.ui.Button, interaction: ApplicationCommandInteraction):
        dice = random.randint(1,6)
        embed = disnake.Embed(title="<:dice:1063065362763096104> | 擲骰子!",description="你擲到了 `{}`".format(dice),colour=disnake.Colour.random())
        await interaction.response.edit_message(embed=embed, view=self)

class Dice(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        super().__init__()
    @commands.Cog.listener()
    async def on_ready(self):
        print("Dice Ready!")

    @commands.slash_command(name="dice", description="來骰骰子!",name_localizations={"zh-TW":"擲骰趣"})
    async def dice(self, interaction: ApplicationCommandInteraction):
        global dice
        global message
        dice = random.randint(1,6)
        embed = disnake.Embed(title="<:dice:1063065362763096104> | 擲骰子!",description="你擲到了 `{}`".format(dice),colour=disnake.Colour.random())
        view = View() 
        message = await interaction.response.send_message(embed=embed,view=view)

def setup(bot):
    bot.add_cog(Dice(bot))