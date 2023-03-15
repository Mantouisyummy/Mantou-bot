import disnake
from disnake.ext import commands
from disnake import ApplicationCommandInteraction
import datetime

# 這邊可以使用Cog功能繼承基本屬性
class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='help',description="help")
    async def help(self, interaction: ApplicationCommandInteraction):
        embed = disnake.Embed(color=disnake.Colour.random(),title="饅頭ㄐ器人", description="指令清單", timestamp= datetime.datetime.utcnow())
        embed.add_field(name="遊戲",value="a", inline=False)
        embed.add_field(name="</剪刀石頭布:1055324151910502521>", value="玩剪刀石頭布", inline=True)
        embed.add_field(name="</attack:1033708946726334485>",value="攻擊你的朋友!",inline=True)
        embed.add_field(name="查詢",value="a", inline=False)
        embed.add_field(name="</頭貼:1055127681588531241>", value="查詢別人的頭貼", inline=True)
        embed.add_field(name="</旗幟:1057301482313105409>", value="查詢別人的旗幟 (目前還沒修好)", inline=True)
        embed.add_field(name="</ping:1039919755185885194>", value="查看我的延遲!", inline=True)
        embed.add_field(name="</credit:1039919755185885194>", value="查看協助的工作人員", inline=True)
        embed.add_field(name="實用",value="a", inline=False)
        embed.add_field(name="</autorole:1024970814782713876>", value="自訂義你的專屬身分組!", inline=True)
        embed.add_field(name="</ticket:1060055858156933120>", value="開啟一個客服單吧!", inline=True)
        embed.add_field(name="音樂", value="a", inline=False)
        embed.add_field(name="</play:1034796068732411914>", value="播歌!", inline=True)
        embed.add_field(name="</nowplaying:1053895111408357406>", value="即時顯示目前撥放的歌曲", inline=True)
        embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
        await interaction.response.send_message(embed=embed)

    async def cog_command_error(interaction: ApplicationCommandInteraction, error):
        embed = disnake.Embed(title=":x: 出現錯誤了!!!", description=f"```{error}```")
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(help(bot))