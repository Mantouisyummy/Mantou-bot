import disnake
from disnake.ext import commands
from disnake import ApplicationCommandInteraction
import datetime
class join(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
    
    @commands.Cog.listener()
    async def on_member_join(self, member:disnake.Member):
        channel = disnake.utils.get(member.guild.channels, id=1024477488405037099)
        embed = disnake.Embed(title=f"歡迎 {member.name} !", description=f"歡迎來到 {member.guild.name} !\n這裡是松農世界計畫的群組~\n希望你在這裡過得很好!", color=disnake.Colour.random(), timestamp= datetime.datetime.utcnow(), url=member.guild.icon.url)
        embed.set_image(url=member.avatar.url)
        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(join(bot))


