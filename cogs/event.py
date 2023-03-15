
import disnake
import random
from disnake.ui import Button
from disnake.ext import commands
from disnake import ApplicationCommandInteraction, Option,VoiceChannel
import datetime
from typing import Optional
import json
import os
import io

# 這邊可以使用Cog功能繼承基本屬性

class UnlockView(disnake.ui.View):
    def __init__(self):
        self.choice = ""
        super().__init__(timeout=None)
    @disnake.ui.button(label="1",style=disnake.ButtonStyle.green,row=0,custom_id="1")
    async def one(self, button: disnake.ui.Button, interaction: ApplicationCommandInteraction):
        if len(self.choice) == 4:
            self.choice = ""
        else:
            pass        
        if self.choice != "":
            self.choice += "1"
            embed = disnake.Embed(title="請輸入密碼",description=f"你輸入的密碼為: {self.choice}",colour=disnake.Colour.random())
            await message.edit(embed=embed)
        else:
            self.choice = "1"
            embed = disnake.Embed(title="請輸入密碼",description=f"你輸入的密碼為: {self.choice}",colour=disnake.Colour.random())
            await message.edit(embed=embed)
        embed = disnake.Embed(title="請輸入密碼",description=f"你輸入的密碼為: {self.choice}",colour=disnake.Colour.random())
        await message.edit(embed=embed)
    @disnake.ui.button(label="2",style=disnake.ButtonStyle.green,row=0,custom_id="2")
    async def two(self, button: disnake.ui.Button, interaction: ApplicationCommandInteraction):
        if len(self.choice) == 4:
            self.choice = ""
        else:
            pass        
        if self.choice != "":
            self.choice += "2"
            embed = disnake.Embed(title="請輸入密碼",description=f"你輸入的密碼為: {self.choice}",colour=disnake.Colour.random())
            await message.edit(embed=embed)
        else:
            self.choice = "2"
            embed = disnake.Embed(title="請輸入密碼",description=f"你輸入的密碼為: {self.choice}",colour=disnake.Colour.random())
            await message.edit(embed=embed)
        embed = disnake.Embed(title="請輸入密碼",description=f"你輸入的密碼為: {self.choice}",colour=disnake.Colour.random())
        await message.edit(embed=embed)
    @disnake.ui.button(label="3",style=disnake.ButtonStyle.green,row=0,custom_id="3")
    async def three(self, button: disnake.ui.Button, interaction: ApplicationCommandInteraction):
        if len(self.choice) == 4:
            self.choice = ""
        else:
            pass        
        if self.choice != "":
            self.choice += "3"
            embed = disnake.Embed(title="請輸入密碼",description=f"你輸入的密碼為: {self.choice}",colour=disnake.Colour.random())
            await message.edit(embed=embed)
        else:
            self.choice = "3"
            embed = disnake.Embed(title="請輸入密碼",description=f"你輸入的密碼為: {self.choice}",colour=disnake.Colour.random())
            await message.edit(embed=embed)
        embed = disnake.Embed(title="請輸入密碼",description=f"你輸入的密碼為: {self.choice}",colour=disnake.Colour.random())
        await message.edit(embed=embed)
    @disnake.ui.button(label="4",style=disnake.ButtonStyle.green,row=1,custom_id="4")
    async def four(self, button: disnake.ui.Button, interaction: ApplicationCommandInteraction):
        if len(self.choice) == 4:
            self.choice = ""
        else:
            pass        
        if self.choice != "":
            self.choice += "4"
            embed = disnake.Embed(title="請輸入密碼",description=f"你輸入的密碼為: {self.choice}",colour=disnake.Colour.random())
            await message.edit(embed=embed)
        else:
            self.choice = "4"
            embed = disnake.Embed(title="請輸入密碼",description=f"你輸入的密碼為: {self.choice}",colour=disnake.Colour.random())
            await message.edit(embed=embed)
        embed = disnake.Embed(title="請輸入密碼",description=f"你輸入的密碼為: {self.choice}",colour=disnake.Colour.random())
        await message.edit(embed=embed)
    @disnake.ui.button(label="5",style=disnake.ButtonStyle.green,row=1,custom_id="5")
    async def five(self, button: disnake.ui.Button, interaction: ApplicationCommandInteraction):
        if len(self.choice) == 4:
            self.choice = ""
        else:
            pass        
        if self.choice != "":
            self.choice += "5"
            embed = disnake.Embed(title="請輸入密碼",description=f"你輸入的密碼為: {self.choice}",colour=disnake.Colour.random())
            await message.edit(embed=embed)
        else:
            self.choice = "5"
            embed = disnake.Embed(title="請輸入密碼",description=f"你輸入的密碼為: {self.choice}",colour=disnake.Colour.random())
            await message.edit(embed=embed)
        embed = disnake.Embed(title="請輸入密碼",description=f"你輸入的密碼為: {self.choice}",colour=disnake.Colour.random())
        await message.edit(embed=embed)
    @disnake.ui.button(label="6",style=disnake.ButtonStyle.green,row=1,custom_id="6")
    async def six(self, button: disnake.ui.Button, interaction: ApplicationCommandInteraction):
        if len(self.choice) == 4:
            self.choice = ""
        else:
            pass        
        if self.choice != "":
            self.choice += "6"
            embed = disnake.Embed(title="請輸入密碼",description=f"你輸入的密碼為: {self.choice}",colour=disnake.Colour.random())
            await message.edit(embed=embed)
        else:
            self.choice = "6"
            embed = disnake.Embed(title="請輸入密碼",description=f"你輸入的密碼為: {self.choice}",colour=disnake.Colour.random())
            await message.edit(embed=embed)
        embed = disnake.Embed(title="請輸入密碼",description=f"你輸入的密碼為: {self.choice}",colour=disnake.Colour.random())
        await message.edit(embed=embed)
    @disnake.ui.button(label="7",style=disnake.ButtonStyle.green,row=3,custom_id="7")
    async def seven(self, button: disnake.ui.Button, interaction: ApplicationCommandInteraction):
        if len(self.choice) == 4:
            self.choice = ""
        else:
            pass        
        if self.choice != "":
            self.choice += "7"
            embed = disnake.Embed(title="請輸入密碼",description=f"你輸入的密碼為: {self.choice}",colour=disnake.Colour.random())
            await message.edit(embed=embed)
        else:
            self.choice = "7"
            embed = disnake.Embed(title="請輸入密碼",description=f"你輸入的密碼為: {self.choice}",colour=disnake.Colour.random())
            await message.edit(embed=embed)
        embed = disnake.Embed(title="請輸入密碼",description=f"你輸入的密碼為: {self.choice}",colour=disnake.Colour.random())
        await message.edit(embed=embed)
    @disnake.ui.button(label="8",style=disnake.ButtonStyle.green,row=3,custom_id="8")
    async def eight(self, button: disnake.ui.Button, interaction: ApplicationCommandInteraction):
        if len(self.choice) == 4:
            self.choice = ""
        else:
            pass        
        if self.choice != "":
            self.choice += "8"
            embed = disnake.Embed(title="請輸入密碼",description=f"你輸入的密碼為: {self.choice}",colour=disnake.Colour.random())
            await message.edit(embed=embed)
        else:
            self.choice = "8"
            embed = disnake.Embed(title="請輸入密碼",description=f"你輸入的密碼為: {self.choice}",colour=disnake.Colour.random())
            await message.edit(embed=embed)
        embed = disnake.Embed(title="請輸入密碼",description=f"你輸入的密碼為: {self.choice}",colour=disnake.Colour.random())
        await message.edit(embed=embed)
    @disnake.ui.button(label="9",style=disnake.ButtonStyle.green,row=3,custom_id="9")
    async def nine(self, button: disnake.ui.Button, interaction: ApplicationCommandInteraction):
        if len(self.choice) == 4:
            self.choice = ""
        else:
            pass        
        if self.choice != "":
            self.choice += "9"
            embed = disnake.Embed(title="請輸入密碼",description=f"你輸入的密碼為: {self.choice}",colour=disnake.Colour.random())
            await message.edit(embed=embed)
        else:
            self.choice = "9"
            embed = disnake.Embed(title="請輸入密碼",description=f"你輸入的密碼為: {self.choice}",colour=disnake.Colour.random())
            await message.edit(embed=embed)
        embed = disnake.Embed(title="請輸入密碼",description=f"你輸入的密碼為: {self.choice}",colour=disnake.Colour.random())
        await message.edit(embed=embed)

    @disnake.ui.button(label="刪除",style=disnake.ButtonStyle.red,row=4,emoji="<a:no:1010010462391382066>",custom_id="delete")
    async def delete(self, button: disnake.ui.Button, interaction: ApplicationCommandInteraction):
        self.choice = self.choice[:-1]
        embed = disnake.Embed(title="請輸入密碼",description=f"你輸入的密碼為: {self.choice}",colour=disnake.Colour.random())
        await message.edit(embed=embed)

    @disnake.ui.button(label="0",style=disnake.ButtonStyle.green,row=4,custom_id="0")
    async def zero(self, button: disnake.ui.Button, interaction: ApplicationCommandInteraction):
        if len(self.choice) == 4:
            self.choice = ""
        else:
            pass        
        if self.choice != "":
            self.choice += "0"
            embed = disnake.Embed(title="請輸入密碼",description=f"你輸入的密碼為: {self.choice}",colour=disnake.Colour.random())
            await message.edit(embed=embed)
        else:
            self.choice = "0"
            embed = disnake.Embed(title="請輸入密碼",description=f"你輸入的密碼為: {self.choice}",colour=disnake.Colour.random())
            await message.edit(embed=embed)
    

    @disnake.ui.button(label="確定",style=disnake.ButtonStyle.blurple,row=4,emoji="<a:check:1043896950484902009>",custom_id="confirm")
    async def Confirm(self, button: disnake.ui.Button, interaction: ApplicationCommandInteraction):
        if password == self.choice:
            overwrite = voice_channel.overwrites_for(interaction.user)
            overwrite.connect = True
            await voice_channel.set_permissions(interaction.user,overwrite=overwrite)
            embed = disnake.Embed(title="<:check:1036160202174627840> | 密碼正確",colour=disnake.Colour.green())
            await interaction.response.send_message(embed=embed,ephemeral=True)
            self.stop()

        else:
            embed = disnake.Embed(title="<:x_mark:1033955039615664199> | 密碼錯誤",colour=disnake.Colour.red())
            await interaction.response.send_message(embed=embed,ephemeral=True)
            self.choice = ""
        embed = disnake.Embed(title="請輸入密碼",description=f"你輸入的密碼為: {self.choice}",colour=disnake.Colour.random())
        await message.edit(embed=embed)
    
    

class Modal(disnake.ui.Modal):
    def __init__(self):
        super().__init__("請輸入密碼")
    
        self.password = disnake.ui.TextInput(
                label="請輸入四位數密碼 (可留空)",
                min_length=4,
                max_length=4,
                required=False
            )
        self.add_item(self.password)

    async def callback(self, interaction: ApplicationCommandInteraction):
        global join_channel
        global message_channel
        global password
        try:
            get_channel = disnake.utils.get(interaction.guild.voice_channels, id=join_channel.id)
        except NameError:
            pass
        try:
            if get_channel is not None:
                failed_embed = disnake.Embed(title="<:x_mark:1033955039615664199> | 你已經有這個頻道了!",description=f"你的頻道在 {get_channel.mention}",colour=disnake.Colour.red())
                await interaction.response.send_message(embed=failed_embed,ephemeral=True)
            else:
                if self.password.value == "":
                    number = random.randint(0000,9999)
                    password = number
                    embed = disnake.Embed(title=f":lock: | 已成功鎖定!",description=f"密碼為 `{password}`!",colour=disnake.Colour.green())
                    embed.add_field(name=f"鎖定的頻道",value=f"{voice_channel.mention}")
                    await interaction.response.send_message(embed=embed,ephemeral=True)
                    overwrite = voice_channel.overwrites_for(interaction.guild.default_role)
                    overwrite.connect = False
                    await voice_channel.set_permissions(interaction.guild.default_role,overwrite=overwrite)
                    if voice_channel.category is None:
                        pass
                    else:
                        channel_id = interaction.channel.id
                        message_channel = disnake.utils.get(interaction.guild.text_channels,id=channel_id)
                        join_channel = await interaction.guild.create_voice_channel(name=f"進入此頻道以加入 {voice_channel.name}",category=voice_channel.category)
                    if os.path.isfile(f"./database/guild/{interaction.guild.id}.json"):
                        with open(f"./database/guild/{interaction.guild.id}.json",encoding='utf-8') as f:
                            data = json.load(f)
                            if data["Guildname"] != "":
                                data["encryption_channel"] = join_channel.id
                            else:
                                data["Guildname"] = interaction.guild.name
                                data["encryption_channel"] = join_channel.id
                            with open(f"./database/guild/{interaction.guild.id}.json","w",encoding='utf-8') as f:
                                json.dump(data,f)
                                
                    else:
                        with open(f"./database/guild/{interaction.guild.id}.json","w+",encoding='utf-8') as f:
                            f.write(json.dumps({"Guildname":"","encryption_channel":""}))
                        with open(f"./database/guild/{interaction.guild.id}.json",encoding='utf-8') as f:
                            data = json.load(f)
                        if data["Guildname"] != "":
                            data["encryption_channel"] = join_channel.id
                        else:
                            data["Guildname"] = interaction.guild.name
                            data["encryption_channel"] = join_channel.id
                        with open(f"./database/guild/{interaction.guild.id}.json","w",encoding='utf-8') as f:
                            json.dump(data,f)

                else:
                    password = self.password.value
                    embed = disnake.Embed(title=f":lock: | 已成功鎖定!",description=f"密碼為 `{self.password.value}`!",colour=disnake.Colour.green())
                    embed.add_field(name=f"頻道",value=f"{voice_channel.mention}")
                    await interaction.response.send_message(embed=embed,ephemeral=True)
                    overwrite = voice_channel.overwrites_for(interaction.guild.default_role)
                    overwrite.connect = False
                    await voice_channel.set_permissions(interaction.guild.default_role,overwrite=overwrite)
                    if voice_channel.category is None:
                        pass
                    else:
                        channel_id = interaction.channel.id
                        message_channel = disnake.utils.get(interaction.guild.text_channels,id=channel_id)
                        join_channel = await interaction.guild.create_voice_channel(name=f"進入此頻道以加入 {voice_channel.name}",category=voice_channel.category)
                    if os.path.isfile(f"./database/guild/{interaction.guild.id}.json"):
                        with open(f"./database/guild/{interaction.guild.id}.json",encoding='utf-8') as f:
                            data = json.load(f)
                            if data["Guildname"] != "":
                                data["encryption_channel"] = join_channel.id
                            else:
                                data["Guildname"] = interaction.guild.name
                                print(data["Guildname"])
                                data["encryption_channel"] = join_channel.id
                            with open(f"./database/guild/{interaction.guild.id}.json","w",encoding='utf-8') as f:
                                json.dump(data,f)
                    
                    else:
                        with open(f"./database/guild/{interaction.guild.id}.json","w+",encoding='utf-8') as f:
                            f.write(json.dumps({"Guildname":"","encryption_channel":""}))
                        with open(f"./database/guild/{interaction.guild.id}.json",encoding='utf-8') as f:
                            data = json.load(f)
                        if data["Guildname"] != "":
                            data["encryption_channel"] = join_channel.id
                        else:
                            data["Guildname"] = interaction.guild.name
                            print(data["Guildname"])
                            data["encryption_channel"] = join_channel.id
                        with open(f"./database/guild/{interaction.guild.id}.json","w",encoding='utf-8') as f:
                            json.dump(data,f)
        except UnboundLocalError:
            if self.password.value == "":
                    number = random.randint(0000,9999)
                    password = number
                    embed = disnake.Embed(title=f":lock: | 已成功鎖定!",description=f"密碼為 `{password}`!",colour=disnake.Colour.green())
                    embed.add_field(name=f"頻道",value=f"{voice_channel.mention}")
                    await interaction.response.send_message(embed=embed,ephemeral=True)
                    overwrite = voice_channel.overwrites_for(interaction.guild.default_role)
                    overwrite.connect = False
                    await voice_channel.set_permissions(interaction.guild.default_role,overwrite=overwrite)
                    if voice_channel.category is None:
                        pass
                    else:
                        channel_id = interaction.channel.id
                        message_channel = disnake.utils.get(interaction.guild.text_channels,id=channel_id)
                        join_channel = await interaction.guild.create_voice_channel(name=f"進入此頻道以加入 {voice_channel.name}",category=voice_channel.category)
                    if os.path.isfile(f"./database/guild/{interaction.guild.id}.json"):
                        with open(f"./database/guild/{interaction.guild.id}.json",encoding='utf-8') as f:
                            data = json.load(f)
                        if data["Guildname"] != "":
                            data["encryption_channel"] = join_channel.id
                        else:
                            data["Guildname"] = interaction.guild.name
                            print(data["Guildname"])
                            data["encryption_channel"] = join_channel.id
                        with open(f"./database/guild/{interaction.guild.id}.json","w",encoding='utf-8') as f:
                            json.dump(data,f)
                    else:
                        with open(f"./database/guild/{interaction.guild.id}.json","w+",encoding='utf-8') as f:
                            f.write(json.dumps({"Guildname":"","encryption_channel":""}))
                        with open(f"./database/guild/{interaction.guild.id}.json",encoding='utf-8') as f:
                            data = json.load(f)
                        if data["Guildname"] != "":
                            data["encryption_channel"] = join_channel.id
                        else:
                            data["Guildname"] = interaction.guild.name
                            print(data["Guildname"])
                            data["encryption_channel"] = join_channel.id
                        with open(f"./database/guild/{interaction.guild.id}.json","w",encoding='utf-8') as f:
                            json.dump(data,f)

            else:
                password = self.password.value
                embed = disnake.Embed(title=f":lock: | 已成功鎖定!",description=f"密碼為 `{self.password.value}`!",colour=disnake.Colour.green())
                embed.add_field(name=f"頻道",value=f"{voice_channel.mention}")
                await interaction.response.send_message(embed=embed,ephemeral=True)
                overwrite = voice_channel.overwrites_for(interaction.guild.default_role)
                overwrite.connect = False
                await voice_channel.set_permissions(interaction.guild.default_role,overwrite=overwrite)
                if voice_channel.category is None:
                    pass
                else:
                    channel_id = interaction.channel.id
                    message_channel = disnake.utils.get(interaction.guild.text_channels,id=channel_id)
                    join_channel = await interaction.guild.create_voice_channel(name=f"進入此頻道以加入 {voice_channel.name}",category=voice_channel.category)
                if os.path.isfile(f"./database/guild/{interaction.guild.id}.json"):
                    with open(f"./database/guild/{interaction.guild.id}.json",encoding='utf-8') as f:
                        data = json.load(f)
                        if data["Guildname"] != "":
                            data["encryption_channel"] = join_channel.id
                        else:
                            data["Guildname"] = interaction.guild.name
                            data["encryption_channel"] = join_channel.id
                        with open(f"./database/guild/{interaction.guild.id}.json","w",encoding='utf-8') as f:
                            json.dump(data,f)
                                           
                else:
                    with open(f"./database/guild/{interaction.guild.id}.json","w+",encoding='utf-8') as f:
                        f.write(json.dumps({"Guildname":"","encryption_channel":""}))
                    with open(f"./database/guild/{interaction.guild.id}.json",encoding='utf-8') as f:
                        data = json.load(f)
                        if data["Guildname"] != "":
                            data["encryption_channel"] = join_channel.id
                        else:
                            data["Guildname"] = interaction.guild.name
                            data["encryption_channel"] = join_channel.id
                    with open(f"./database/guild/{interaction.guild.id}.json","w",encoding='utf-8') as f:
                        json.dump(data,f)




class enc(commands.Cog): #加密頻道
    def __init__(self, bot:commands.Bot):
        super().__init__()
        self.bot = bot
	
    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(UnlockView())
        print("Enc Ready!")
    
    @commands.Cog.listener()
    async def on_voice_state_update(self, member:disnake.Member, before, after):
        global message
        try:
            with open(f"./database/guild/{say.guild.id}.json","r",encoding='utf-8') as f:
                data = json.load(f)
            voice_channel = disnake.utils.get(say.guild.voice_channels,id=data["encryption_channel"]) 
        except NameError:
            return
        view = UnlockView()
        if not before.channel and after.channel:
            for channel in member.guild.voice_channels:
                if channel.name == voice_channel.name:
                    global message
                    embed = disnake.Embed(title="請輸入密碼",colour=disnake.Colour.random())
                    message = await message_channel.send(embed=embed,view=view)
                    await view.wait()
        else:
            await message.delete()                      

    @commands.slash_command(name='lock',description="加密伺服器上的任何一個頻道",name_localizations={"zh-TW":"加密頻道"})
    @commands.has_permissions(manage_channels=True)
    async def enc(self, interaction: ApplicationCommandInteraction, channel:Optional[VoiceChannel]= Option(name="頻道",required=True)):
        global say
        global voice_channel
        voice_channel = channel
        say = interaction
        model = Modal()
        await interaction.response.send_modal(modal=model)
def setup(bot):
    bot.add_cog(enc(bot))