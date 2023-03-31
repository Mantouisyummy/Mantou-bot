import disnake
from typing import Optional
from disnake.ext import commands
from disnake import ApplicationCommandInteraction, Option, OptionType,Embed,Colour
import pymongo
import json
import os
import math
from datetime import timezone, timedelta

def adv_eval(id, new:dict):
    myclient = pymongo.MongoClient("mongodb://mongo:sHG7YDV0nMasrjtAuQ3m@containers-us-west-188.railway.app:6917")
    mydb = myclient['adventure']
    mycol = mydb["user"]
    eval_data = {"ID": { "$regex": f"^{id}" }}
    eval_new = { "$set": new }
    mycol.update_one(eval_data,eval_new)

def database(guild):
    with open(f"./database/guild/{guild}.json",encoding='utf-8') as f:
        data = json.load(f)
    return data


    
class ExceptionHandler(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Error_Handle Ready!")

    @commands.Cog.listener()
    async def on_slash_command_error(self, interaction: ApplicationCommandInteraction, error) -> None:
        print(error)
        if isinstance(error, commands.MissingPermissions):
            embed = disnake.Embed(title="<:x_mark:1033955039615664199> 無法執行此指令", description=f"請確認您是否有 `{error}` 的權限",colour=disnake.Colour.red())
            await interaction.response.send_message(embed=embed,ephemeral=True)
        elif isinstance(error, commands.ChannelNotFound):
            embed = disnake.Embed(title="<:x_mark:1033955039615664199> 找不到此頻道",colour=disnake.Colour.red())
            await interaction.response.send_message(embed=embed,ephemeral=True)
        elif isinstance(error, commands.RoleNotFound):
            embed = disnake.Embed(title="<:x_mark:1033955039615664199> 找不到此身分組",colour=disnake.Colour.red())
            await interaction.response.send_message(embed=embed,ephemeral=True)
        elif isinstance(error, disnake.NotFound):
            embed = disnake.Embed(title=f"<:x_mark:1033955039615664199> 找不到 {error}",colour=disnake.Colour.red())
            await interaction.response.send_message(embed=embed,ephemeral=True)
        elif isinstance(error, commands.BotMissingPermissions):
            embed = disnake.Embed(title=f"<:x_mark:1033955039615664199> 機器人沒有 {error} 的權限",colour=disnake.Colour.red())
            await interaction.response.send_message(embed=embed,ephemeral=True)
        elif isinstance(error, commands.CommandOnCooldown):
            pass
        else:
            embed = disnake.Embed(title=":x: 阿喔，看來你用神奇魔法發現了一個漏洞 <:hahahaha:1038449572915187763>", description=f"```{error}```\n <a:853174934670540811:1038449712359022643> 已自動回報給作者! Bug反饋可以聯繫Man頭(´・ω・)#8870",colour=disnake.Colour.red())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.response.send_message(embed=embed)

    @commands.slash_command(name='eval', description="噓~",guild_ids=[1003837176464810115])
    async def eval(self, interaction: ApplicationCommandInteraction, option:str = Option(name="噓",description="噓")):
        if interaction.user.id == 549056425943629825:
            #ticket_channel = disnake.utils.get(self.bot.get_guild(int(guild_id)).text_channels,id=int(channel_id))
            #conversation_record = await ticket_channel.history(limit=int(limit)).flatten()
            #text = ""
            #for message in conversation_record:
                #now = message.created_at.astimezone(timezone(offset = timedelta(hours = 8)))
                #text = f"{now.year}/{now.month}/{now.day} {now.hour}:{now.minute} - {message.author.display_name}: {message.content}\n{text}"
            #with open(f"chat.txt",'w',encoding='UTF-8') as chat:
                #chat.write(text)
            print(eval(option))
            try:
                embed = disnake.Embed(title=":white_check_mark: | 神秘的結果", description="```py\n{}```".format(eval(option)),colour=disnake.Colour.green())
                await interaction.response.send_message(embed=embed)
            except disnake.errors.HTTPException:
                with open(f"eval.txt",'w',encoding='UTF-8') as chat:
                    chat.write(str(eval(option))) #將訊息寫入至chat.txt
                embed = disnake.Embed(title=":white_check_mark: | 神秘的結果", description="因字數過多,已轉成文件",colour=disnake.Colour.green())
                await interaction.response.send_message(embed=embed,file=disnake.File(f"eval.txt"))
                os.remove(f"chat.txt")
        else:
            embed = disnake.Embed(title=":x: | 這個指令太過邪惡了,只有饅頭能夠駕馭他 (?")
            await interaction.response.send_message(embed=embed)
    
    @commands.slash_command(name="load_extension",guild_ids=[1003837176464810115],options=[Option(name="extension",description="噓",type=OptionType.string,required=True)])
    async def load(self,interaction: ApplicationCommandInteraction, extension:str):
        if interaction.user.id == 549056425943629825:
            for fn in os.listdir("./cogs"):
                if fn.endswith(".py"):
                    self.bot.load_extension(f"cogs.{extension}")
            embed = Embed(title="<:check:1036160202174627840> | 加載成功!",description=f"目標cog:{extension}",colour=Colour.green())
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("你不是擁有者!",ephemeral=True)
    
    @commands.slash_command(name="unload_extension",guild_ids=[1003837176464810115],options=[Option(name="extension",description="噓",type=OptionType.string,required=True)])
    async def unload(self,interaction: ApplicationCommandInteraction, extension:str):
        if interaction.user.id == 549056425943629825:
            for fn in os.listdir("./cogs"):
                if fn.endswith(".py"):
                    self.bot.unload_extension(f"cogs.{extension}")
            embed = Embed(title="<:check:1036160202174627840> | 卸載成功!",description=f"目標cog:{extension}",colour=Colour.green())
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("你不是擁有者!",ephemeral=True)
    
    @commands.slash_command(name="reload_extension",guild_ids=[1003837176464810115],options=[Option(name="extension",description="噓",type=OptionType.string,required=True)])
    async def reload(self,interaction: ApplicationCommandInteraction, extension:str):
        if interaction.user.id == 549056425943629825:
            for fn in os.listdir("./cogs"):
                if fn.endswith(".py"):
                    self.bot.reload_extension(f"cogs.{extension}")
            embed = Embed(title="<:check:1036160202174627840> | 重新載入成功!",description=f"目標cog:{extension}",colour=Colour.green())
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("你不是擁有者!",ephemeral=True)

    
        
        
def setup(bot):
    bot.add_cog(ExceptionHandler(bot))
