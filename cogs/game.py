import disnake
from disnake.ext import commands
from disnake import ApplicationCommandInteraction
import datetime
import numpy as np
import math
# 這邊可以使用Cog功能繼承基本屬性



class Subscriptions(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = None
        self.win = 0
        self.lose = 0
        self.list = []
        self.dict = {"石頭":"布","剪刀":"石頭","布":"剪刀"}
        self.round = 0
        self.choice = None
    
    @disnake.ui.button(label= "✂️", style=disnake.ButtonStyle.green)
    async def Scissors(self, button: disnake.ui.Button, interaction: ApplicationCommandInteraction):
        if Player != str(interaction.user.id):
            embed = disnake.Embed(title=":x: | 又不是你在玩", colour=disnake.Colour.red())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.response.send_message(embed=embed, ephemeral=True)
        if Player == str(interaction.user.id):
            self.round += 1
            self.value = False
            self.choice = "剪刀"
            user_result = self.choice
            #電腦判斷區
            Dict = {"石頭":self.list.count("石頭"),"剪刀":self.list.count("剪刀"),"布":self.list.count("布")}
            global computer_choice
            if len(set(Dict.values())) == 1: #玩家三种出拳记录一样，电脑随机出拳
                computer_choice = np.random.choice(["剪刀","石頭","布"])
            elif len(set(Dict.values())) == 2:
                m = min(Dict.values())
                if list(Dict.values()).count(m) == 1: #两大一小，随机选择两大之一
                    for key in Dict.keys():
                        if Dict[key] == m:
                            tempL = list(set(["石頭","剪刀","布",])-set([key,]))
                            computer_choice = self.dict[np.random.choice(tempL)]
                            break
                else: #两小一大，直接取最大
                    m = max(Dict.values())
                    for key in Dict.keys():
                        if Dict[key] == m:
                            computer_choice = self.dict[key]
                            break
            else: #玩家三种出拳记录各不相等，取出拳次数最多的
                m = max(Dict.values())
                for key in Dict.keys():
                    if Dict[key] == m:
                        computer_choice = self.dict[key]
                        break
            self.list.append(self.choice)
            computer_result = computer_choice
            embed = disnake.Embed(color=disnake.Colour.random(), title="🤖 | 剪刀石頭布",description=f"<:trophy:1033707678654005358> 勝利場數: {self.win} 場")
            if ((computer_result == "布" and user_result == "剪刀") or (computer_result == "石頭" and user_result == "布") or (computer_result == "剪刀" and user_result == "石頭")): #玩家贏了
                embed.add_field(name="你出了", value="{}".format(user_result), inline=False)
                embed.add_field(name="我出了", value="{}".format(computer_result), inline=False)
                embed.add_field(name="結果", value="你贏了!", inline=False)
                self.win += 1
                embed.set_footer(text=f"目前勝率 {math.floor((self.win / self.round) * 100)}% | 第{self.round}回合", icon_url=avatar)
                await interaction.response.edit_message(embed=embed)
            elif user_result == computer_result:
                embed.add_field(name="你出了", value="{}".format(user_result), inline=False)
                embed.add_field(name="我出了", value="{}".format(computer_result), inline=False)
                embed.add_field(name="結果", value="平手!", inline=False)
                embed.set_footer(text=f"目前勝率 {math.floor((self.win / self.round) * 100)}% | 第{self.round}回合", icon_url=avatar)
                await interaction.response.edit_message(embed=embed)
            else:
                embed.add_field(name="你出了", value="{}".format(user_result), inline=False)
                embed.add_field(name="我出了", value="{}".format(computer_result), inline=False)
                embed.add_field(name="結果", value="我贏了!", inline=False)
                embed.set_footer(text=f"目前勝率 {math.floor((self.win / self.round) * 100)}% | 第{self.round}回合", icon_url=avatar)
                self.lose +=1
                await interaction.response.edit_message(embed=embed)

    @disnake.ui.button(label = "🪨", style=disnake.ButtonStyle.red)
    async def rock(self, button: disnake.ui.Button, interaction: ApplicationCommandInteraction):
        if Player != str(interaction.user.id):
            embed = disnake.Embed(title=":x: | 又不是你在玩", colour=disnake.Colour.red())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.response.send_message(embed=embed, ephemeral=True)
        if Player == str(interaction.user.id):
            self.round += 1
            self.value = False
            self.choice = "石頭"
            user_result = self.choice
            #電腦判斷區
            Dict = {"石頭":self.list.count("石頭"),"剪刀":self.list.count("剪刀"),"布":self.list.count("布")}
            global computer_choice
            if len(set(Dict.values())) == 1: #玩家三种出拳记录一样，电脑随机出拳
                computer_choice = np.random.choice(["剪刀","石頭","布"])
            elif len(set(Dict.values())) == 2:
                m = min(Dict.values())
                if list(Dict.values()).count(m) == 1: #两大一小，随机选择两大之一
                    for key in Dict.keys():
                        if Dict[key] == m:
                            tempL = list(set(["石頭","剪刀","布",])-set([key,]))
                            computer_choice = self.dict[np.random.choice(tempL)]
                            break
                else: #两小一大，直接取最大
                    m = max(Dict.values())
                    for key in Dict.keys():
                        if Dict[key] == m:
                            computer_choice = self.dict[key]
                            break
            else: #玩家三种出拳记录各不相等，取出拳次数最多的
                m = max(Dict.values())
                for key in Dict.keys():
                    if Dict[key] == m:
                        computer_choice = self.dict[key]
                        break
            self.list.append(self.choice)
            computer_result = computer_choice
            embed = disnake.Embed(color=disnake.Colour.random(), title="🤖 | 剪刀石頭布",description=f"<:trophy:1033707678654005358> 勝利場數: {self.win} 場")
            if ((computer_result == "布" and user_result == "剪刀") or (computer_result == "石頭" and user_result == "布") or (computer_result == "剪刀" and user_result == "石頭")): #玩家贏了
                embed.add_field(name="你出了", value="{}".format(user_result), inline=False)
                embed.add_field(name="我出了", value="{}".format(computer_result), inline=False)
                embed.add_field(name="結果", value="你贏了!", inline=False)
                self.win += 1
                embed.set_footer(text=f"目前勝率 {math.floor((self.win / self.round) * 100)}% | 第{self.round}回合", icon_url=avatar)
                await interaction.response.edit_message(embed=embed)
            elif user_result == computer_result:
                embed.add_field(name="你出了", value="{}".format(user_result), inline=False)
                embed.add_field(name="我出了", value="{}".format(computer_result), inline=False)
                embed.add_field(name="結果", value="平手!", inline=False)
                embed.set_footer(text=f"目前勝率 {math.floor((self.win / self.round) * 100)}% | 第{self.round}回合", icon_url=avatar)
                await interaction.response.edit_message(embed=embed)
            else:
                embed.add_field(name="你出了", value="{}".format(user_result), inline=False)
                embed.add_field(name="我出了", value="{}".format(computer_result), inline=False)
                embed.add_field(name="結果", value="我贏了!", inline=False)
                self.lose +=1
                embed.set_footer(text=f"目前勝率 {math.floor((self.win / self.round) * 100)}% | 第{self.round}回合", icon_url=avatar)
                await interaction.response.edit_message(embed=embed)

    @disnake.ui.button(label = "🖐", style=disnake.ButtonStyle.blurple)
    async def paper(self, button: disnake.ui.Button, interaction: ApplicationCommandInteraction):
        if Player != str(interaction.user.id):
            embed = disnake.Embed(title=":x: | 又不是你在玩", colour=disnake.Colour.red())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.response.send_message(embed=embed, ephemeral=True)
        if Player == str(interaction.user.id):
            self.round += 1
            self.value = False
            self.choice = "布"
            user_result = self.choice
            #電腦判斷區
            Dict = {"石頭":self.list.count("石頭"),"剪刀":self.list.count("剪刀"),"布":self.list.count("布")}
            global computer_choice
            if len(set(Dict.values())) == 1: #玩家三种出拳记录一样，电脑随机出拳
                computer_choice = np.random.choice(["剪刀","石頭","布"])
            elif len(set(Dict.values())) == 2:
                m = min(Dict.values())
                if list(Dict.values()).count(m) == 1: #两大一小，随机选择两大之一
                    for key in Dict.keys():
                        if Dict[key] == m:
                            tempL = list(set(["石頭","剪刀","布",])-set([key,]))
                            computer_choice = self.dict[np.random.choice(tempL)]
                            break
                else: #两小一大，直接取最大
                    m = max(Dict.values())
                    for key in Dict.keys():
                        if Dict[key] == m:
                            computer_choice = self.dict[key]
                            break
            else: #玩家三种出拳记录各不相等，取出拳次数最多的
                m = max(Dict.values())
                for key in Dict.keys():
                    if Dict[key] == m:
                        computer_choice = self.dict[key]
                        break
            self.list.append(self.choice)
            computer_result = computer_choice
            embed = disnake.Embed(color=disnake.Colour.random(), title="🤖 | 剪刀石頭布",description=f"<:trophy:1033707678654005358> 勝利場數: {self.win} 場")
            if ((computer_result == "布" and user_result == "剪刀") or (computer_result == "石頭" and user_result == "布") or (computer_result == "剪刀" and user_result == "石頭")): #玩家贏了
                embed.add_field(name="你出了", value="{}".format(user_result), inline=False)
                embed.add_field(name="我出了", value="{}".format(computer_result), inline=False)
                embed.add_field(name="結果", value="你贏了!", inline=False)
                self.win += 1
                embed.set_footer(text=f"目前勝率 {math.floor((self.win / self.round) * 100)}% | 第{self.round}回合", icon_url=avatar)
                await interaction.response.edit_message(embed=embed)
            elif user_result == computer_result:
                embed.add_field(name="你出了", value="{}".format(user_result), inline=False)
                embed.add_field(name="我出了", value="{}".format(computer_result), inline=False)
                embed.add_field(name="結果", value="平手!", inline=False)
                embed.set_footer(text=f"目前勝率 {math.floor((self.win / self.round) * 100)}% | 第{self.round}回合", icon_url=avatar)
                await interaction.response.edit_message(embed=embed)
            else:
                embed.add_field(name="你出了", value="{}".format(user_result), inline=False)
                embed.add_field(name="我出了", value="{}".format(computer_result), inline=False)
                embed.add_field(name="結果", value="我贏了!", inline=False)
                self.lose +=1
                embed.set_footer(text=f"目前勝率 {math.floor((self.win / self.round) * 100)}% | 第{self.round}回合", icon_url=avatar)
                await interaction.response.edit_message(embed=embed)
class game(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.slash_command(name='rps',description="就是個剪刀石頭布",name_localizations={"zh-TW":"剪刀石頭布"})
    async def rps(self, interaction: ApplicationCommandInteraction):
        global Player
        global avatar
        avatar = self.bot.user.avatar.url
        Player = str(interaction.user.id)
        view = Subscriptions()
        embed = disnake.Embed(color=disnake.Colour.random(), title="🤖 | 剪刀石頭布",description="你要出啥呢?")
        await interaction.response.send_message(embed=embed, view=view)
        await view.wait()

def setup(bot):
    bot.add_cog(game(bot))
