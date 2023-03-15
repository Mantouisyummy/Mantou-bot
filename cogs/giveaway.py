import disnake
from disnake.ext import commands
from disnake import ApplicationCommandInteraction,Option
import random
import asyncio

class View(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.list = []
        self.already_join = False
    
    @disnake.ui.button(label="🎉參加抽獎",style=disnake.ButtonStyle.green,custom_id="join")
    async def join(self, button: disnake.ui.Button, interaction: ApplicationCommandInteraction):
        global member_list
        if state == "Start":
            if interaction.user.id in self.list:
                embed = disnake.Embed(title="<:x_mark:1033955039615664199> | 你已經參加了!",colour=disnake.Colour.red())
                await interaction.response.send_message(embed=embed,ephemeral=True)
            else:
                self.list.append(interaction.user.id)
                print(self.list)
                member_list = self.list
                embed = disnake.Embed(title="<:check:1036160202174627840> | 參加抽獎成功!",colour=disnake.Colour.green())
                await interaction.response.send_message(embed=embed,ephemeral=True)

    @disnake.ui.button(label="抽獎名單",style=disnake.ButtonStyle.gray,custom_id="join_list")
    async def join_list(self, button: disnake.ui.Button, interaction: ApplicationCommandInteraction):
        embed = disnake.Embed(title="目前的參加名單",description=f"共有 `{len(self.list)}` 位參加了抽獎!",colour=disnake.Colour.random())
        await interaction.response.send_message(embed=embed,ephemeral=True)
    
class EndView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=0)

    @disnake.ui.button(label="🎉已結束",style=disnake.ButtonStyle.green,custom_id="end",disabled=True)
    async def join(self, button: disnake.ui.Button, interaction: ApplicationCommandInteraction):
        pass

class Giveaway(commands.Cog):
    def __init__(self,bot:commands.Bot):
        self.bot = bot
        self.state = None
        super().__init__()
    
    
    @commands.slash_command(name="giveaway",description="透過此指令來創立一個抽獎!",name_localizations={"zh-TW":"抽獎"},guild_ids=[947837498321670185])
    async def giveaway(self, interaction: ApplicationCommandInteraction,name:str = Option(name="標題",description="就 打標題",required=True),endtime:str = Option(name="結束時間",description="可打1d 1s 1h",required=True),people:int = Option(name="指定更多的中獎人數",description="沒有就例外",required=False)):
        self.state = "Start"
        global state
        global remain_time
        global host
        host = interaction.user
        state = self.state
        if people is None:
            people = 1
        elif people < 0:
            await interaction.response.send_message("你抽負數的人是想幹嘛?")
            return
        if endtime.endswith("d"):
            view = View()
            remain_time = endtime.removesuffix("d") 
            embed = disnake.Embed(title=f"{name} - 抽{people}位",description=f"將於 `{remain_time}` 天後 結束抽獎!",colour=disnake.Colour.random())
            giveaway_message = await interaction.response.send_message(embed=embed,view=view)
            await asyncio.sleep(60*60*24*int(remain_time))
            if people > 1:
                winner = random.choices(member_list,k=people)
                for i in winner:
                    member = self.bot.get_user(i)
            else:
                winner = random.choice(member_list)
                member = self.bot.get_user(winner)
            self.state = "End"
            state = self.state
            success_embed = disnake.Embed(title=f"{name} - 抽{people}位",description=f"抽獎已結束",colour=disnake.Colour.random())
            await giveaway_message.edit(embed=success_embed,view=view)
            await interaction.followup.send(f"請 {member.mention} 找 {host.mention} 領獎!")
        elif endtime.endswith("s"):
            view = View()
            remain_time = endtime.removesuffix("s") 
            embed = disnake.Embed(title=f"{name} - 抽{people}位",description=f"將於 `{remain_time}` 秒後 結束抽獎!",colour=disnake.Colour.random())
            giveaway_message = await interaction.response.send_message(embed=embed,view=view)
            await asyncio.sleep(int(remain_time))
            if people > 1:
                winner = random.choices(member_list,k=people)
                for i in winner:
                    member = self.bot.get_user(i)
            else:
                winner = random.choice(member_list)
                member = self.bot.get_user(winner)
            self.state = "End"
            state = self.state
            success_embed = disnake.Embed(title=f"{name} - 抽{people}位",description=f"抽獎已結束",colour=disnake.Colour.random())
            endview = EndView()
            await giveaway_message.edit(embed=success_embed,view=endview)
            await interaction.followup.send(f"請 {member.mention} 找 {host.mention} 領獎!")
        elif endtime.endswith("h"):
            view = View()
            remain_time = endtime.removesuffix("h")
            embed = disnake.Embed(title=f"{name} - 抽{people}位",description=f"將於 `{remain_time}` 小時後 結束抽獎!",colour=disnake.Colour.random())
            giveaway_message = await interaction.response.send_message(embed=embed,view=view)
            await asyncio.sleep(60*60*int(remain_time))
            if people > 1:
                winner = random.choices(member_list,k=people)
                for i in winner:
                    member = self.bot.get_user(i)
            else:
                winner = random.choice(member_list)
                member = self.bot.get_user(winner)
            self.state = "End"
            state = self.state
            success_embed = disnake.Embed(title=f"{name} - 抽{people}位",description=f"抽獎已結束",colour=disnake.Colour.random())
            endview = EndView()
            await giveaway_message.edit(embed=success_embed,view=endview)
            await interaction.followup.send(f"請 {member.mention} 找 {host.mention} 領獎!")
        elif endtime.endswith("m"):
            view = View()
            remain_time = endtime.removesuffix("m")
            embed = disnake.Embed(title=f"{name} - 抽{people}位",description=f"將於 `{remain_time}` 分鐘後 結束抽獎!",colour=disnake.Colour.random())
            giveaway_message = await interaction.response.send_message(embed=embed,view=view)
            await asyncio.sleep(60*int(remain_time))
            if people > 1:
                print(people)
                winner = random.choices(member_list,k=people)
                for i in winner:
                    print(i)
                    member = self.bot.get_user(i)
            else:
                winner = random.choice(member_list)
                print(winner)
                member = self.bot.get_user(winner)
            self.state = "End"
            state = self.state
            success_embed = disnake.Embed(title=f"{name} - 抽{people}位",description=f"抽獎已結束",colour=disnake.Colour.random())
            endview = EndView()
            await giveaway_message.edit(embed=success_embed,view=endview)
            await interaction.followup.send(f"請 {member.mention} 找 {host.mention} 領獎!")
        else:
            await interaction.response.send_message("請輸入正確的時間格式!",ephemeral=True)

def setup(bot):
    bot.add_cog(Giveaway(bot))
            