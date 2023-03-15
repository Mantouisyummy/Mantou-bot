import disnake
from disnake.ext import commands
from disnake import ApplicationCommandInteraction,Option,OptionType,Embed,Colour
import random
class Question(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        super().__init__()
    @commands.Cog.listener()
    async def on_ready(self):
        print("Question Ready!")

    @commands.slash_command(name="question", description="由鰻頭ㄐ器人給你最好的回答",name_localizations={"zh-TW":"問問題"},options=[Option(name="question",description="打你要問的問題",type=OptionType.string,required=True)],auto_sync=True)
    async def question(self, interaction: ApplicationCommandInteraction,question:str):
        answer_list = ["我覺得就是了(ﾉ>ω<)ﾉ","我覺得不是ㄟ",f"我覺得應該有{random.randint(0,100)}%的可能是(･ω´･ )",f"我覺得應該有{random.randint(0,100)}%的可能不是( ͡° ͜ʖ ͡°)","等我買到了鰻頭在跟你講答案(｡A｡)","偶不知道(´・ω・`)"]
        answer = random.choice(answer_list)
        embed = Embed(title=f"問題<:cutefox:1033313959203323924> | {question}",description=f"{answer}",colour=Colour.random())
        await interaction.response.send_message(embed=embed)
        

def setup(bot):
    bot.add_cog(Question(bot))