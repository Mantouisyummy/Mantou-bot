import disnake
from disnake.ext import commands
from disnake import ApplicationCommandInteraction,Option,OptionType,MessageInteraction,Member
from typing import Optional
import datetime
import random
import json
import os

class Unmarry(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @disnake.ui.button(label="確定", style=disnake.ButtonStyle.green,custom_id="unmarry_agree",emoji="<:Daiyousei_cry:1047789114025582673>")
    async def unmarry_agree(self, button: disnake.ui.Button, interaction: ApplicationCommandInteraction):
        pass

    @disnake.ui.button(label="我再想想", style=disnake.ButtonStyle.red,custom_id="unmarry_deny",emoji="<a:Loading:1059806500241027157>")
    async def unmarry_deny(self, button: disnake.ui.Button, interaction: ApplicationCommandInteraction):
        pass

class View(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @disnake.ui.button(label="答應!", style=disnake.ButtonStyle.green,custom_id="agree",emoji="<a:heartcat:972907092258197594>")
    async def agree(self, button: disnake.ui.Button, interaction: ApplicationCommandInteraction):
        pass

    @disnake.ui.button(label="拒絕", style=disnake.ButtonStyle.red,custom_id="deny")
    async def deny(self, button: disnake.ui.Button, interaction: ApplicationCommandInteraction):
        pass
    

class Marry(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        self.suitor = None
        self.member = None
        super().__init__()
    @commands.Cog.listener()
    async def on_ready(self):
        print("Marry Ready!")

    @commands.slash_command(name="marry", description="求婚!",options=[Option(name="member",description="你要求婚的對象",type=OptionType.user,required=True),Option(name="message",description="給對方的告白話",type=OptionType.string,required=False)])
    async def marry(self, interaction: ApplicationCommandInteraction,member:Optional[Member],message:Optional[str] = Option(name="message",description="給對方的告白話",type=OptionType.string,required=False)):
        if os.path.isfile(f"./database/users/{interaction.user.id}.json"):
            pass
        else:
            with open(f"./database/users/{interaction.user.id}.json","w+",encoding='utf-8') as f:
                f.write(json.dumps({"marry_user":"","marry_time":""}))
        if os.path.isfile(f"./database/users/{member.id}.json"):
            pass
        else:
            with open(f"./database/users/{member.id}.json","w+",encoding='utf-8') as f:
                f.write(json.dumps({"marry_user":"","marry_time":""}))
        with open(f"./database/users/{interaction.user.id}.json",encoding='utf-8') as f:
            data = json.load(f)
        with open(f"./database/users/{member.id}.json",encoding='utf-8') as f:
            try:
                data_2 = json.load(f)
            except KeyError:
                with open(f"./database/users/{member.id}.json","w+",encoding='utf-8') as f:
                    f.write(json.dumps({"marry_user":"","marry_time":""}))
                with open(f"./database/users/{member.id}.json",encoding='utf-8') as f:
                     data_2 = json.load(f)
        try:
            if data["marry_user"] == "" and data_2["marry_user"] == "":
                if interaction.user.id != member.id:
                    self.suitor = interaction.user
                    self.member = member
                    if type(message) == str:
                        embed = disnake.Embed(title=f":rose: | {interaction.user.name} 跟你求婚!",description=f"{interaction.user.mention} 想對 {member.mention} 說的告白話:\n{message}",colour=disnake.Colour.random())
                        view = View() 
                        await interaction.response.send_message(content=f"{member.mention}",embed=embed,view=view)
                    else:
                        embed = disnake.Embed(title=f":rose: | {interaction.user.name} 跟你求婚!",description=f"是否同意?",colour=disnake.Colour.random())
                        view = View() 
                        await interaction.response.send_message(content=f"{member.mention}",embed=embed,view=view)
                else:
                    embed = disnake.Embed(title=f":x: | 你不能自己跟自己結婚!",colour=disnake.Colour.red())
                    await interaction.response.send_message(embed=embed)
            elif data["marry_user"] == "" and data_2["marry_user"] != "":
                embed = disnake.Embed(title=f":x: | 你要結婚的對象已經有人了!",colour=disnake.Colour.red())
                await interaction.response.send_message(embed=embed)
            elif data["marry_user"] != "" and data_2["marry_user"] != "" or data["marry_user"] != "" and data_2["marry_user"] == "":
                embed = disnake.Embed(title=f":x: | 不要偷找小三!",colour=disnake.Colour.red())
                await interaction.response.send_message(embed=embed)
        except KeyError:
            with open(f"./database/users/{interaction.user.id}.json","w+",encoding='utf-8') as f:
                f.write(json.dumps({"marry_user":"","marry_time":""}))
            if data["marry_user"] == "" and data_2["marry_user"] == "":
                if interaction.user.id != member.id:
                    self.member = member
                    embed = disnake.Embed(title=f":rose: | {interaction.user.name} 跟你求婚!",description="是否同意?",colour=disnake.Colour.random())
                    view = View() 
                    await interaction.response.send_message(content=f"{member.mention}",embed=embed,view=view)
                else:
                    embed = disnake.Embed(title=f":x: | 你不能自己跟自己結婚!",colour=disnake.Colour.red())
                    await interaction.response.send_message(embed=embed)
            elif data["marry_user"] == "" and data_2["marry_user"] != "":
                embed = disnake.Embed(title=f":x: | 你要結婚的對象已經有人了!",colour=disnake.Colour.red())
                await interaction.response.send_message(embed=embed)
            elif data["marry_user"] != "" and data_2["marry_user"] != "" or data["marry_user"] != "" and data_2["marry_user"] == "":
                embed = disnake.Embed(title=f":x: | 不要偷找小三!",colour=disnake.Colour.red())
                await interaction.response.send_message(embed=embed)
        
    @commands.slash_command(name="unmarry", description="離婚")
    async def unmarry(self, interaction: ApplicationCommandInteraction):
        if os.path.isfile(f"./database/users/{interaction.user.id}.json"):
            pass
        else:
            with open(f"./database/users/{interaction.user.id}.json","w+",encoding='utf-8') as f:
                f.write(json.dumps({"marry_user":"","marry_time":""}))
        with open(f"./database/users/{interaction.user.id}.json",encoding='utf-8') as f:
            data = json.load(f)
        try:
            if data["marry_user"] != "":
                    love = data["marry_user"]
                    user = self.bot.get_user(love)
                    embed = disnake.Embed(title=f":x: | 你確定要跟 {user.name} 離婚嗎!?",colour=disnake.Colour.red())
                    view = Unmarry() 
                    await interaction.response.send_message(content=f"{interaction.user.mention}",embed=embed,view=view)
            else:
                embed = disnake.Embed(title=f":x: | 你沒有對象可以離婚喔 建議去找一個 (x",colour=disnake.Colour.red())
                await interaction.response.send_message(embed=embed)
        except KeyError:
            embed = disnake.Embed(title=f":x: | 你沒有對象可以離婚喔 建議去找一個 (x",colour=disnake.Colour.red())
            await interaction.response.send_message(embed=embed)
            
    
    @commands.Cog.listener(name="on_message_interaction")
    async def on_message_interaction(self, interaction: MessageInteraction):
            match interaction.data.custom_id:
                case "agree":
                    if interaction.user.id == self.member.id:
                        loc_dt = datetime.datetime.today() 
                        time_del = datetime.timedelta(hours=3) 
                        new_dt = loc_dt + time_del 
                        datetime_format = new_dt.strftime("%Y/%m/%d %H:%M:%S")
                        with open(f"./database/users/{self.suitor.id}.json",encoding='utf-8') as f:
                            data = json.load(f)
                            data["marry_user"] = self.member.id
                            data["marry_time"] = datetime_format
                        with open(f"./database/users/{self.suitor.id}.json","w",encoding='utf-8') as f:
                            json.dump(data,f)
                        with open(f"./database/users/{self.member.id}.json",encoding='utf-8') as f:
                            data_2 = json.load(f)
                            data_2["marry_user"] = self.suitor.id
                            data_2["marry_time"] = datetime_format
                        with open(f"./database/users/{self.member.id}.json","w",encoding='utf-8') as f:
                            json.dump(data_2,f)
                        love = data["marry_user"]
                        embed = disnake.Embed(title=f"🎊🎊皆大歡喜!",description=f"恭喜 {self.suitor.mention} 和 <@{love}> 結為夫妻!",colour=disnake.Colour.green())
                        await interaction.response.edit_message(content=None,embed=embed,view=None)
                    else:
                        embed = disnake.Embed(title=":x: | 不要擅自決定阿喂!",colour=disnake.Colour.red())
                        await interaction.response.send_message(embed=embed,ephemeral=True)
                case "deny":
                    if interaction.user.id == self.member.id:
                        embed = disnake.Embed(title=":x: | 求婚被拒絕了",colour=disnake.Colour.red())
                        await interaction.response.edit_message(content=None,embed=embed,view=None)
                    else:
                        embed = disnake.Embed(title=":x: | 不要擅自決定阿喂!",colour=disnake.Colour.red())
                        await interaction.response.send_message(embed=embed,ephemeral=True)
                case "unmarry_agree":
                    with open(f"./database/users/{interaction.user.id}.json",encoding='utf-8') as f:
                        data = json.load(f)
                    love = data["marry_user"]
                    with open(f"./database/users/{love}.json",encoding='utf-8') as f:
                        data_2 = json.load(f)
                    love_2 = data_2["marry_user"]
                    if interaction.user.id == love_2:
                        embed = disnake.Embed(title=f":x: | 喔不",description=f"<@{love_2}> 和 <@{love}> 離婚了:(",colour=disnake.Colour.green())
                        await interaction.response.edit_message(content=None,embed=embed,view=None)

                        with open(f"./database/users/{love}.json",encoding='utf-8') as f:
                            data = json.load(f)
                            data["marry_user"] = ""
                            data["marry_time"] = ""
                        with open(f"./database/users/{love}.json","w",encoding='utf-8') as f:
                            json.dump(data,f)
                        with open(f"./database/users/{love_2}.json",encoding='utf-8') as f:
                            data_2 = json.load(f)
                            data_2["marry_user"] = ""
                            data_2["marry_time"] = ""
                        with open(f"./database/users/{love_2}.json","w",encoding='utf-8') as f:
                            json.dump(data,f)
                    else:
                        embed = disnake.Embed(title=":x: | 不要擅自決定阿喂!",colour=disnake.Colour.red())
                        await interaction.response.send_message(embed=embed,ephemeral=True)
                case "unmarry_deny":
                    with open(f"./database/users/{interaction.user.id}.json",encoding='utf-8') as f:
                        data = json.load(f)
                    love = data["marry_user"]
                    with open(f"./database/users/{love}.json",encoding='utf-8') as f:
                        data_2 = json.load(f)
                    love_2 = data_2["marry_user"]
                    if interaction.user.id == love_2:
                        embed = disnake.Embed(title=":x: | 你拒絕了離婚",colour=disnake.Colour.red())
                        await interaction.response.edit_message(content=None,embed=embed,view=None)
                    else:
                        embed = disnake.Embed(title=":x: | 不要擅自決定阿喂!",colour=disnake.Colour.red())
                        await interaction.response.send_message(embed=embed,ephemeral=True)
def setup(bot):
    bot.add_cog(Marry(bot))