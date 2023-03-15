import disnake
from disnake.ext import commands
from disnake import ApplicationCommandInteraction, Member, Option
from typing import Optional
import time
import datetime
import requests
import json
import os

class View(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.default_avatar = True

    @disnake.ui.button(label="伺服器頭貼",style=disnake.ButtonStyle.green,emoji="<:loop:1035850844958105660>")
    async def avatar(self,button: disnake.ui.Button, interaction: ApplicationCommandInteraction):
        if self.default_avatar == True:
            if member.guild_avatar != None:
                button.label = "個人頭貼"
                button.style = disnake.ButtonStyle.green
                self.default_avatar = False
                embed = disnake.Embed(title=f"{member.name} 的伺服器頭貼",colour=disnake.Colour.random())
                embed.set_image(url=member.guild_avatar.url)
                await interaction.response.edit_message(embed=embed,view=self)
            else:
                button.label = "沒有伺服器頭貼!"
                button.style = disnake.ButtonStyle.red
                button.disabled = True
                await interaction.response.edit_message(view=self)
        else:
            button.label = "伺服器頭貼"
            button.style = disnake.ButtonStyle.blurple
            self.default_avatar = True
            embed = disnake.Embed(title=f"{member.name} 的個人頭貼",colour=disnake.Colour.random())
            embed.set_image(url=member.avatar.url)
            await interaction.response.edit_message(embed=embed,view=self)





class Info(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        super().__init__()

    @commands.slash_command(name="info",description="透過ID查別人",name_localizations={"zh-TW":"查看使用者資訊"})
    async def userinfo(self,interaction: ApplicationCommandInteraction, target:Optional[Member] = Option(name="target",description="放你要查的人ID",required=True)):
        global member
        member = target
        if type(target) == Member:
            if str(target).isdigit:
                if os.path.isfile(f"./database/users/{target.id}.json"):
                    with open(f"./database/users/{target.id}.json","r",encoding='utf-8') as f:
                        data = json.load(f)
                        print(data)
                    embed = disnake.Embed(title=f"{target.name}#{target.discriminator}",colour=disnake.Colour.random())
                    embed.add_field(name="用戶ID",value=f"`{target.id}`",inline=False)
                    createdate_time = ((str(target.created_at.hour) +":"+ str(target.created_at.minute)))
                    createdate_date = (str(target.created_at.date()).replace('-','/') + ' '+ createdate_time)
                    joindate_time = ((str(target.joined_at.hour) +":"+ str(target.joined_at.minute)))
                    joindate_date = (str(target.joined_at.date()).replace('-','/') + ' '+ joindate_time)
                    print(createdate_time)
                    create_timestamp = time.mktime(datetime.datetime.strptime(createdate_date, "%Y/%m/%d %H:%M").timetuple())
                    join_timestamp = time.mktime(datetime.datetime.strptime(joindate_date, "%Y/%m/%d %H:%M").timetuple())
                    embed.add_field(name="帳號創立時間",value=f"<t:{int(create_timestamp)}>" ,inline=True)
                    embed.add_field(name="加入群組時間",value=f"<t:{int(join_timestamp)}>",inline=False)
                    try:
                        if data == "" or data["marry_user"] == "":
                            embed.add_field(name=":heart: 感情狀態",value=f"單身",inline=False)
                        else:
                            love = data["marry_user"]
                            try:
                                love_timestamp = time.mktime(datetime.datetime.strptime(data["marry_time"],"%Y/%m/%d %H:%M:%S").timetuple())
                                embed.add_field(name=":heart: 感情狀態",value=f"已和 <@{love}> 結婚!\n結婚時間<t:{int(love_timestamp)}>",inline=False)
                            except KeyError:
                                embed.add_field(name=":heart: 感情狀態",value=f"已和 <@{love}> 結婚!",inline=False)
                        embed.set_thumbnail(url=target.avatar.url)
                        await interaction.response.send_message(embed=embed)
                    except KeyError:
                        embed.add_field(name=":heart: 感情狀態",value=f"單身",inline=False)
                        embed.set_thumbnail(url=target.avatar.url)
                        await interaction.response.send_message(embed=embed)
                else:
                    with open(f"./database/users/{interaction.user.id}.json","a+",encoding='utf-8') as f:
                        f.write(json.dumps({}))

            else:
                if os.path.isfile(f"./database/users/{target.id}.json"):
                    with open(f"./database/users/{target.id}.json","r",encoding='utf-8') as f:
                        data = json.load(f)
                    embed = disnake.Embed(title=f"{target.name}#{target.discriminator}",colour=disnake.Colour.random())
                    embed.add_field(name="用戶ID",value=f"`{target.id}`",inline=False)
                    createdate_time = ((str(target.created_at.hour) +":"+ str(target.created_at.minute)))
                    createdate_date = (str(target.created_at.date()).replace('-','/') + ' '+ createdate_time)
                    joindate_time = ((str(target.joined_at.hour) +":"+ str(target.joined_at.minute)))
                    joindate_date = (str(target.joined_at.date()).replace('-','/') + ' '+ joindate_time)
                    print(createdate_time)
                    create_timestamp = time.mktime(datetime.datetime.strptime(createdate_date, "%Y/%m/%d %H:%M").timetuple())
                    join_timestamp = time.mktime(datetime.datetime.strptime(joindate_date, "%Y/%m/%d %H:%M").timetuple())
                    embed.add_field(name="帳號創立時間",value=f"<t:{int(create_timestamp)}>" ,inline=True)
                    embed.add_field(name="加入群組時間",value=f"<t:{int(join_timestamp)}>",inline=False)
                    try:
                        if data == "" or data["marry_user"] == "":
                            embed.add_field(name=":heart: 感情狀態",value=f"單身",inline=False)
                        else:
                            love = data["marry_user"]
                            try:
                                love_timestamp = time.mktime(datetime.datetime.strptime(data["marry_time"],"%Y/%m/%d %H:%M:%S").timetuple())
                                embed.add_field(name=":heart: 感情狀態",value=f"已和 <@{love}> 結婚!\n結婚時間<t:{int(love_timestamp)}>",inline=False)
                            except KeyError:
                                embed.add_field(name=":heart: 感情狀態",value=f"已和 <@{love}> 結婚!",inline=False)
                        embed.set_thumbnail(url=target.avatar.url)
                        await interaction.response.send_message(embed=embed)
                    except KeyError:
                        embed.add_field(name=":heart: 感情狀態",value=f"單身",inline=False)
                        embed.set_thumbnail(url=target.avatar.url)
                        await interaction.response.send_message(embed=embed)
                else:
                    with open(f"./database/users/{interaction.user.id}.json","w+",encoding='utf-8') as f:
                        f.write(json.dumps({}))

        else:
            target = disnake.utils.get(interaction.guild.members,id=interaction.user.id)
            if str(target).isdigit:
                if os.path.isfile(f"./database/users/{interaction.user.id}.json"):
                    with open(f"./database/users/{interaction.user.id}.json","r",encoding='utf-8') as f:
                        data = json.load(f)
                        print(data)
                    embed = disnake.Embed(title=f"{target.name}#{target.discriminator}",colour=disnake.Colour.random())
                    embed.add_field(name="用戶ID",value=f"`{target.id}`",inline=False)
                    createdate_time = ((str(target.created_at.hour) +":"+ str(target.created_at.minute)))
                    createdate_date = (str(target.created_at.date()).replace('-','/') + ' '+ createdate_time)
                    joindate_time = ((str(target.joined_at.hour) +":"+ str(target.joined_at.minute)))
                    joindate_date = (str(target.joined_at.date()).replace('-','/') + ' '+ joindate_time)
                    print(createdate_time)
                    create_timestamp = time.mktime(datetime.datetime.strptime(createdate_date, "%Y/%m/%d %H:%M").timetuple())
                    join_timestamp = time.mktime(datetime.datetime.strptime(joindate_date, "%Y/%m/%d %H:%M").timetuple())
                    embed.add_field(name="帳號創立時間",value=f"<t:{int(create_timestamp)}>" ,inline=True)
                    embed.add_field(name="加入群組時間",value=f"<t:{int(join_timestamp)}>",inline=False)
                    try:
                        if data == "" or data["marry_user"] == "":
                            embed.add_field(name=":heart: 感情狀態",value=f"單身",inline=False)
                        else:
                            love = data["marry_user"]
                            embed.add_field(name=":heart: 感情狀態",value=f"已和 <@{love}> 結婚!",inline=False)
                        embed.set_thumbnail(url=target.avatar.url)
                        await interaction.response.send_message(embed=embed)
                    except KeyError:
                        embed.add_field(name=":heart: 感情狀態",value=f"單身",inline=False)
                        embed.set_thumbnail(url=target.avatar.url)
                        await interaction.response.send_message(embed=embed)
                else:
                    with open(f"./database/users/{interaction.user.id}.json","w+",encoding='utf-8') as f:
                        f.write(json.dumps({}))

            else:
                if os.path.isfile(f"./database/users/{interaction.user.id}.json"):
                    with open(f"./database/users/{interaction.user.id}.json","r",encoding='utf-8') as f:
                        data = json.load(f)
                    embed = disnake.Embed(title=f"{target.name}#{target.discriminator}",colour=disnake.Colour.random())
                    embed.add_field(name="用戶ID",value=f"`{target.id}`",inline=False)
                    createdate_time = ((str(target.created_at.hour) +":"+ str(target.created_at.minute)))
                    createdate_date = (str(target.created_at.date()).replace('-','/') + ' '+ createdate_time)
                    joindate_time = ((str(target.joined_at.hour) +":"+ str(target.joined_at.minute)))
                    joindate_date = (str(target.joined_at.date()).replace('-','/') + ' '+ joindate_time)
                    print(createdate_time)
                    create_timestamp = time.mktime(datetime.datetime.strptime(createdate_date, "%Y/%m/%d %H:%M").timetuple())
                    join_timestamp = time.mktime(datetime.datetime.strptime(joindate_date, "%Y/%m/%d %H:%M").timetuple())
                    embed.add_field(name="帳號創立時間",value=f"<t:{int(create_timestamp)}>" ,inline=True)
                    embed.add_field(name="加入群組時間",value=f"<t:{int(join_timestamp)}>",inline=False)
                    try:
                        if data == "" or data["marry_user"] == "":
                            embed.add_field(name=":heart: 感情狀態",value=f"單身",inline=False)
                        else:
                            love = data["marry_user"]
                            try:
                                love_timestamp = time.mktime(datetime.datetime.strptime(data["marry_time"],"%Y/%m/%d %H:%M:%S").timetuple())
                                embed.add_field(name=":heart: 感情狀態",value=f"已和 <@{love}> 結婚!\n結婚時間<t:{int(love_timestamp)}>",inline=False)
                            except KeyError:
                                embed.add_field(name=":heart: 感情狀態",value=f"已和 <@{love}> 結婚!",inline=False)
                        embed.set_thumbnail(url=target.avatar.url)
                        await interaction.response.send_message(embed=embed)
                    except KeyError:
                        embed.add_field(name=":heart: 感情狀態",value=f"單身",inline=False)
                        embed.set_thumbnail(url=target.avatar.url)
                        await interaction.response.send_message(embed=embed)

                else:
                    with open(f"./database/users/{interaction.user.id}.json","w+",encoding='utf-8') as f:
                        f.write(json.dumps({}))
        
    @commands.slash_command(name="avatar",description="透過ID查別人",force_global=True,name_localizations={"zh-TW":"頭像"})
    async def avatar(self,interaction: ApplicationCommandInteraction, target:Optional[Member] = Option(name="target",description="放你要查的人ID")):
        global member
        global request
        request = self.bot.http.request
        member = target
        if str(target).isdigit:
            if type(target) == Member:
                embed = disnake.Embed(title=f"{target.name} 的個人頭貼",colour=disnake.Colour.random())
                embed.set_image(url=target.avatar.url)
                view = View()
                await interaction.response.send_message(embed=embed, view=view)
            else:
                member = interaction.user
                embed = disnake.Embed(title=f"{interaction.user.name} 的個人頭貼",colour=disnake.Colour.random())
                embed.set_image(url=interaction.user.avatar.url)
                view = View()
                await interaction.response.send_message(embed=embed, view=view)
        else:
            embed = disnake.Embed(title=f"{target.name} 的個人頭貼",colour=disnake.Colour.random())
            embed.set_image(url=target.avatar.url)
            view = View()
            await interaction.response.send_message(embed=embed, view=view)
    

    @commands.slash_command(name="banner",description="透過ID查別人",force_global=True,name_localizations={"zh-TW":"旗幟"})
    async def banner(self,interaction: ApplicationCommandInteraction, target:Optional[Member] = Option(name="target",description="放你要查的人ID")):
        global member
        global guild_target
        guild_target = target
        if str(target).isdigit:
            if type(target) == Member:
                try:
                    member = await self.bot.fetch_user(target.id)
                    embed = disnake.Embed(title=f"{target.name} 的個人旗幟",colour=disnake.Colour.random())
                    embed.set_image(url=member.banner.url)
                    await interaction.response.send_message(embed=embed)
                except AttributeError:
                    embed = disnake.Embed(title=f"<:x_mark:1033955039615664199> | 指定的使用者沒有旗幟!",colour=disnake.Colour.red())
                    await interaction.response.send_message(embed=embed)

            else:
                try:
                    member = await self.bot.fetch_user(interaction.user.id)
                    embed = disnake.Embed(title=f"{interaction.user.name} 的個人旗幟",colour=disnake.Colour.random())
                    embed.set_image(url=member.banner.url)
                    await interaction.response.send_message(embed=embed)
                except AttributeError:
                    embed = disnake.Embed(title=f"<:x_mark:1033955039615664199> | 指定的使用者沒有旗幟!",colour=disnake.Colour.red())
                    await interaction.response.send_message(embed=embed)
        else:
            try:
                embed = disnake.Embed(title=f"{target.name} 的個人旗幟",colour=disnake.Colour.random())
                embed.set_image(url=member.banner.url)
                await interaction.response.send_message(embed=embed)
            except AttributeError:
                embed = disnake.Embed(title=f"<:x_mark:1033955039615664199> | 指定的使用者沒有旗幟!",colour=disnake.Colour.red())
                await interaction.response.send_message(embed=embed)

    @commands.slash_command(name="credit",description="查看協助的工作人員")
    async def credit(self,interaction: ApplicationCommandInteraction):
        embed = disnake.Embed(title="工作人員名單",colour=disnake.Colour.orange())
        embed.add_field(name="開發人員",value="Man頭(´・ω・)#8870")
        embed.add_field(name="感謝名單",value="凱恩Kane#5384\n待新增...",inline=False)
        await interaction.response.send_message(embed=embed)
                
def setup(bot):
    bot.add_cog(Info(bot))