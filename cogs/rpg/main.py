import disnake
import json
import datetime
import random
import time
import pytz

from disnake.ext import commands
from disnake import ApplicationCommandInteraction, Option, OptionType, MessageInteraction, Member, Embed,Colour, OptionChoice,User
from typing import Optional
from datetime import timedelta,timezone
from .core.functions import initialization,add_money,remove_money,update_bag,translate,now_work
from dateutil.parser import parse # 引入dateutil套件

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self,obj)

class Rpg(commands.Cog):
    def __init__(self,bot:commands.Bot):
        super().__init__()
        self.bot = bot
        self.frequency = 1 #工作次數
        self.backpack_list = []
        self.limit_list = []

    @commands.slash_command(name="rpg")
    async def rpg(self, interaction: ApplicationCommandInteraction):
        pass

    @rpg.sub_command(name="money",description="查看你的錢錢")
    async def money(self, interaction: ApplicationCommandInteraction):
        try:
            with open(f"./database/users/{interaction.author.id}.json","r",encoding="utf-8'") as f:
                data = json.load(f)
                money = data["money"]
        except (KeyError,json.decoder.JSONDecodeError,FileNotFoundError):
            await initialization(bot=self.bot, interaction=interaction,id=interaction.author.id,object="nokey")
        try:
            money = data["money"]
            embed = Embed(title="",description=f"你有 `{money}$`",colour=Colour.random(),timestamp=datetime.datetime.utcnow())
            embed.set_author(name=interaction.author.name,icon_url=interaction.author.avatar)
            await interaction.response.send_message(embed=embed)
        except KeyError:
            pass

    @rpg.sub_command(name="backpack",description="查看包包中的物品")
    async def backpack(self, interaction: ApplicationCommandInteraction):
        try:
            with open(f"./database/users/{interaction.author.id}.json","r",encoding="utf-8'") as f:
                data = json.load(f)
                embed = Embed(title="👜 | 包包",colour=Colour.random())
                replace_dict = {"diamond_ore":f"鑽石礦","stone":"石頭","iron_ore":"鐵礦","coal":"煤炭","gold_ore":"黃金礦"}
                inventory = await translate(data["bag"], replace_dict)
                try:
                    if data["bag"] != {}:
                        for category, items in inventory.items():
                            print(items)
                            items_text = "\n".join(f"{key} `x{value}`" for key, value in items.items())
                            embed.add_field(name=category, value=f"{items_text}", inline=False)
                        embed.set_footer(text="機器人作者by 鰻頭", icon_url=self.bot.user.avatar.url)
                        await interaction.response.send_message(embed=embed)
                    else:
                        no_item_embed = Embed(title=":x: | 你的包包沒有東西",colour=Colour.red())
                        await interaction.response.send_message(embed=no_item_embed,ephemeral=True)
                except AttributeError:
                    no_item_embed = Embed(title=":x: | 你的包包沒有東西",colour=Colour.red())
                    await interaction.response.send_message(embed=no_item_embed,ephemeral=True)
        except  (KeyError,json.decoder.JSONDecodeError,FileNotFoundError):
            await initialization(bot=self.bot, interaction=interaction,id=interaction.author.id,object="nokey")
            await interaction.response.defer()


    @rpg.sub_command(name="work",description="工個作吧")
    @commands.cooldown(1,30,commands.BucketType.user)
    async def work(self, interaction: ApplicationCommandInteraction):
        try:
            with open(f"./database/users/{interaction.author.id}.json","r",encoding="utf-8'") as f:
                data = json.load(f)
            item_list = ["鑽石礦","黃金礦","鐵礦","煤炭","石頭"]
            random_ore = random.choices(item_list,weights=[10,15,25,25,35])
            match random_ore:
                case ["鑽石礦"]:
                    await now_work(bot=self.bot, interaction=interaction,id=interaction.author.id)
                    times = data["times"]
                    embed = Embed(title="⛏️ | 又是挖礦的一天! 是鑽石嗎Σ(°Д°;",description=f"你挖到了一個鑽石礦! 你目前工作了`{times}`次!",colour=Colour.blue())
                    embed.set_footer(text="機器人作者by 鰻頭", icon_url=self.bot.user.avatar.url)
                    await interaction.response.send_message(embed=embed)
                    await update_bag(bot=self.bot, interaction=interaction,id=interaction.author.id,category="礦物",item="diamond_ore",limit=1,choice="upload")
                case ["黃金礦"]:
                    await now_work(bot=self.bot, interaction=interaction,id=interaction.author.id)
                    times = data["times"]
                    embed = Embed(title="⛏️ | 又是挖礦的一天! 是黃金ㄟ(ﾉ>ω<)ﾉ",description=f"你挖到了一個黃金礦! 你目前工作了`{times}`次!",colour=Colour.gold())
                    embed.set_footer(text="機器人作者by 鰻頭", icon_url=self.bot.user.avatar.url)
                    await interaction.response.send_message(embed=embed)
                    await update_bag(bot=self.bot, interaction=interaction,id=interaction.author.id,category="礦物",item="gold_ore",limit=1,choice="upload")
                case ["鐵礦"]:
                    await now_work(bot=self.bot, interaction=interaction,id=interaction.author.id)
                    times = data["times"]
                    embed = Embed(title="⛏️ | 又是挖礦的一天! 是鐵ヽ(●´∀`●)ﾉ",description=f"你挖到了一個鐵礦! 你目前工作了`{times}`次!",colour=Colour.from_rgb(r=181,g=154,b=136))
                    embed.set_footer(text="機器人作者by 鰻頭", icon_url=self.bot.user.avatar.url)
                    await interaction.response.send_message(embed=embed)
                    await update_bag(bot=self.bot, interaction=interaction,id=interaction.author.id,category="礦物",item="iron_ore",limit=1,choice="upload")
                case ["煤炭"]:
                    await now_work(bot=self.bot, interaction=interaction,id=interaction.author.id)
                    times = data["times"]
                    embed = Embed(title="⛏️ | 又是挖礦的一天! 好耶煤炭 (｡A｡) (?",description=f"你挖到了一個煤炭! 你目前工作了`{times}`次!")
                    embed.set_footer(text="機器人作者by 鰻頭", icon_url=self.bot.user.avatar.url)
                    await interaction.response.send_message(embed=embed)
                    await update_bag(bot=self.bot, interaction=interaction,id=interaction.author.id,category="礦物",item="coal",limit=1,choice="upload")
                case ["石頭"]:
                    await now_work(bot=self.bot, interaction=interaction,id=interaction.author.id)
                    times = data["times"]
                    embed = Embed(title="⛏️ | 又是挖礦的一天! 石頭...(´ー`)",description=f"你挖到了一顆石頭! 你目前工作了`{times}`次!",colour=Colour.light_gray())
                    embed.set_footer(text="機器人作者by 鰻頭", icon_url=self.bot.user.avatar.url)
                    await interaction.response.send_message(embed=embed)
                    await update_bag(bot=self.bot, interaction=interaction,id=interaction.author.id,category="礦物",item="stone",limit=1,choice="upload")
        except (KeyError,json.decoder.JSONDecodeError,FileNotFoundError):
            print("hayhay")
            await initialization(bot=self.bot, interaction=interaction,id=interaction.author.id,object="nokey")
            print("lol4")
            with open(f"./database/users/{interaction.author.id}.json","r",encoding="utf-8'") as f:
                data = json.load(f)
            item_list = ["鑽石礦","黃金礦","鐵礦","煤炭","石頭"]
            random_ore = random.choices(item_list,weights=[10,15,25,25,35])
            match random_ore:
                case ["鑽石礦"]:
                    await now_work(bot=self.bot, interaction=interaction,id=interaction.author.id)
                    times = data["times"]
                    embed = Embed(title="⛏️ | 又是挖礦的一天! 是鑽石嗎Σ(°Д°;",description=f"你挖到了一個鑽石礦! 你目前工作了`{times}`次!",colour=Colour.blue())
                    embed.set_footer(text="機器人作者by 鰻頭", icon_url=self.bot.user.avatar.url)
                    await interaction.response.send_message(embed=embed)
                    await update_bag(bot=self.bot, interaction=interaction,id=interaction.author.id,category="礦物",item="diamond_ore",limit=1,choice="upload")
                case ["黃金礦"]:
                    await now_work(bot=self.bot, interaction=interaction,id=interaction.author.id)
                    times = data["times"]
                    embed = Embed(title="⛏️ | 又是挖礦的一天! 是黃金ㄟ(ﾉ>ω<)ﾉ",description=f"你挖到了一個黃金礦! 你目前工作了`{times}`次!",colour=Colour.gold())
                    embed.set_footer(text="機器人作者by 鰻頭", icon_url=self.bot.user.avatar.url)
                    await interaction.response.send_message(embed=embed)
                    await update_bag(bot=self.bot, interaction=interaction,id=interaction.author.id,category="礦物",item="gold_ore",limit=1,choice="upload")
                case ["鐵礦"]:
                    await now_work(bot=self.bot, interaction=interaction,id=interaction.author.id)
                    times = data["times"]
                    embed = Embed(title="⛏️ | 又是挖礦的一天! 是鐵ヽ(●´∀`●)ﾉ",description=f"你挖到了一個鐵礦! 你目前工作了`{times}`次!",colour=Colour.from_rgb(r=181,g=154,b=136))
                    embed.set_footer(text="機器人作者by 鰻頭", icon_url=self.bot.user.avatar.url)
                    await interaction.response.send_message(embed=embed)
                    await update_bag(bot=self.bot, interaction=interaction,id=interaction.author.id,category="礦物",item="iron_ore",limit=1,choice="upload")
                case ["煤炭"]:
                    await now_work(bot=self.bot, interaction=interaction,id=interaction.author.id)
                    times = data["times"]
                    embed = Embed(title="⛏️ | 又是挖礦的一天! 好耶煤炭 (｡A｡) (?",description=f"你挖到了一個煤炭! 你目前工作了`{times}`次!")
                    embed.set_footer(text="機器人作者by 鰻頭", icon_url=self.bot.user.avatar.url)
                    await interaction.response.send_message(embed=embed)
                    await update_bag(bot=self.bot, interaction=interaction,id=interaction.author.id,category="礦物",item="coal",limit=1,choice="upload")
                case ["石頭"]:
                    await now_work(bot=self.bot, interaction=interaction,id=interaction.author.id)
                    times = data["times"]
                    embed = Embed(title="⛏️ | 又是挖礦的一天! 石頭...(´ー`)",description=f"你挖到了一顆石頭! 你目前工作了`{times}`次!",colour=Colour.light_gray())
                    embed.set_footer(text="機器人作者by 鰻頭", icon_url=self.bot.user.avatar.url)
                    await interaction.response.send_message(embed=embed)
                    await update_bag(bot=self.bot, interaction=interaction,id=interaction.author.id,category="礦物",item="stone",limit=1,choice="upload")
            
    @commands.Cog.listener()
    async def on_slash_command_error(self, interaction:ApplicationCommandInteraction, error):
        if isinstance(error, commands.CommandOnCooldown):
            with open(f"./database/users/{interaction.author.id}.json","r",encoding="utf-8'") as f:
                data = json.load(f)
            now = time.time() # 獲取當前時間戳
            end = now + error.retry_after # 計算冷卻結束時間戳
            taipei_tz = datetime.timezone(datetime.timedelta(hours=8)) # 創建台北時區物件，偏移量為8小時
            end_taipei = datetime.datetime.fromtimestamp(end, taipei_tz) # 將冷卻結束時間戳轉換成台北時區的datetime物件
            end_str = end_taipei.isoformat() # 將冷卻結束時間轉換成ISO格式的字串
            end_datetime = parse(end_str)
            end_custom = end_datetime.strftime("%Y-%m-%d %H:%M:%S")
            count = data["times"]
            timestamp = end_datetime.timestamp()
            print(timestamp)
            embed = Embed(title=":x: | 你需要休息!",description=f"你目前工作了 `{count}` 次! <t:{int(timestamp)}:R> 才能再次挖礦!",colour=Colour.red())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url=self.bot.user.avatar.url)
            await interaction.response.send_message(embed=embed)


    Items = commands.option_enum({"鑽石礦":"diamond_ore","黃金礦":"gold_ore","鐵礦":"iron_ore","煤炭":"coal","石頭":"stone"})
    @rpg.sub_command(name="sell",description="賣出物品")
    async def sell(self, interaction: ApplicationCommandInteraction,items:Items,limit:int = Option(name="數量",description="要出售的物品數量",type=OptionType.integer)):
        try:
            with open(f"./database/users/{interaction.author.id}.json","r",encoding="utf-8'") as f:
                data = json.load(f)
        except (KeyError,json.decoder.JSONDecodeError,FileNotFoundError):
            await initialization(bot=self.bot, interaction=interaction,id=interaction.author.id,object="nokey")
        print(items)
        print(data["bag"]["礦物"])
        try:
            if items in data["bag"]["礦物"]:
                if limit <= data["bag"]["礦物"][f"{items}"]:
                    await update_bag(bot=self.bot, interaction=interaction,id=interaction.author.id,category="礦物",item=items,limit=limit, choice="sell")
                else:
                    embed = Embed(title=":x: | 你沒有夠多的物品可出售!",colour=Colour.red())
                    await interaction.response.send_message(embed=embed,ephemeral=True)
            else:
                embed = Embed(title=":x: | 你沒有這個礦物可出售!",colour=Colour.red())
                await interaction.response.send_message(embed=embed,ephemeral=True)

        except KeyError:
            pass

    @commands.slash_command(name="add_money",description="增加你的錢錢")
    async def add__money(self, 
                        interaction: ApplicationCommandInteraction,
                        member:Optional[User] = Option(name="member",description="用戶"),
                        add_to_money:int = Option(name="要加的錢",type=OptionType.integer,description="數量")):
        if interaction.user.id == 549056425943629825:
            await add_money(bot=self.bot, interaction=interaction,id=member.id,money=add_to_money)
        else:
            embed = disnake.Embed(title=":x: | 這個指令太過邪惡了,只有饅頭能夠駕馭他 (?",colour=Colour.red())
            await interaction.response.send_message(embed=embed)

    @commands.slash_command(name="remove_money",description="減少你的錢錢")
    async def remove__money(self, 
                        interaction: ApplicationCommandInteraction,
                        member:Optional[User] = Option(name="member",description="用戶"),
                        remove_to_money:int = Option(name="要減的錢",type=OptionType.integer,description="數量")):
        if interaction.user.id == 549056425943629825:
            await remove_money(bot=self.bot, interaction=interaction,id=member.id, money=remove_to_money)
        else:
            embed = disnake.Embed(title=":x: | 這個指令太過邪惡了,只有饅頭能夠駕馭他 (?",colour=Colour.red())
            await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Rpg(bot))
