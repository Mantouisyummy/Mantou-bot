import json
import os 
import datetime
import random

from disnake import Interaction, Message, Thread, TextChannel, Embed, NotFound, Colour, ButtonStyle
from disnake.ext.commands import Bot
from disnake.utils import get

async def initialization(bot:Bot, interaction:Interaction, id:int, object:str):
    if os.path.isfile(f"./database/users/{id}.json"):
        print("hayhayhayhay")
        with open(f"./database/users/{id}.json","r",encoding="utf-8'") as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError:
                with open(f"./database/users/{id}.json","w",encoding='utf-8') as f:
                    f.write(json.dumps({})) 
            if object == "nokey":
                print("lol3")
                with open(f"./database/users/{id}.json","r",encoding='utf-8') as f:
                        data = json.load(f)
                        data["money"] = 0
                        data["stamina"] = 20
                        data["bag"] = {}
                        data["times"] = 1
                with open(f"./database/users/{id}.json","w",encoding='utf-8') as f:
                        json.dump(data,f)
    else:
        with open(f"./database/users/{id}.json","w",encoding="utf-8'") as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError:
                with open(f"./database/users/{id}.json","w",encoding='utf-8') as f:
                    f.write(json.dumps({}))
        with open(f"./database/users/{id}.json","r",encoding='utf-8') as f:
                data = json.load(f)
                data["money"] = 0
                data["stamina"] = 20
                data["bag"] = {}
                data["times"] = 1
        with open(f"./database/users/{id}.json","w",encoding='utf-8') as f:
                json.dump(data,f)

        


async def add_money(bot:Bot, interaction:Interaction, id:int, money:int):
    with open(f"./database/users/{id}.json",encoding="utf-8'") as f:
        data = json.load(f)
    try:
        if interaction.user.id == 549056425943629825:
            new_money = int(data["money"]) + money
            data["money"] = new_money
            with open(f"./database/users/{id}.json","w+",encoding='utf-8') as f:
                    json.dump(data,f,ensure_ascii=False)
            user = get(bot.get_all_members(),id=id)
            embed = Embed(title=f"✅ | 成功",description=f"已給予 {user.name} `{money}$`\n他目前的餘額 `{new_money}$`",colour=Colour.green())
            await interaction.response.send_message(embed=embed)
        else:
             pass
    except KeyError:
        if interaction.user.id == 549056425943629825:
            await initialization(bot,interaction,id,object="nokey")
            await interaction.response.defer()
            money = data["money"]
            new_money = int(data["money"]) + money
            data["money"] = new_money
            with open(f"./database/users/{id}.json","w+",encoding='utf-8') as f:
                    json.dump(data,f,ensure_ascii=False)
            user = get(bot.get_all_members(),id=id)
            embed = Embed(title=f"✅ | 成功",description=f"已給予 {user.name} `{money}$`\n他目前的餘額 `{new_money}$`",colour=Colour.green())
            await interaction.response.send_message(embed=embed)
        else:
            pass


async def remove_money(bot:Bot, interaction:Interaction, id:int, money:int):
    with open(f"./database/users/{id}.json","r",encoding="utf-8'") as f:
        data = json.load(f)
    try:
        if interaction.user.id == 549056425943629825:
            new_money = int(data["money"]) - money
            data["money"] = new_money
            with open(f"./database/users/{id}.json","w+",encoding='utf-8') as f:
                    json.dump(data,f)
            user = get(bot.get_all_members(),id=id)
            embed = Embed(title=f"✅ | 成功",description=f"已減少 {user.name} `{money}$`\n他目前的餘額:`{new_money}$`",colour=Colour.green())
            await interaction.response.send_message(embed=embed)
        else:
             pass
    except KeyError:
        if interaction.user.id == 549056425943629825:
            await initialization(bot,interaction,id,object="nokey")
            await interaction.response.defer()
            money = data["money"]
            with open(f"./database/users/{id}.json","w+",encoding='utf-8') as f:
                    json.dump(data,f)
            user = get(bot.get_all_members(),id=id)
            embed = Embed(title=f"✅ | 成功",description=f"已減少 {user.name} `{money}$`\n他目前的餘額:`{new_money}$`",colour=Colour.green())
            await interaction.response.send_message(embed=embed)
        else:
            pass

async def update_bag(bot:Bot, interaction:Interaction,category:str ,id:int, item:str, limit:int,choice:str):
    with open(f"./database/users/{id}.json","r",encoding="utf-8") as f:
        data = json.load(f)
    try:
        if choice == "upload":
            if data["bag"] == {}: 
                data["bag"] = {f"{category}":{}}
                data["bag"][f"{category}"][f"{item}"] = limit
                with open(f"./database/users/{id}.json","w+",encoding='utf-8') as f:
                        json.dump(data,f)
            else:
                try:
                    # 如果 item 存在，更新 item 的 limit
                    new_limit = data["bag"][f"{category}"][f"{item}"] + limit
                    data["bag"][f"{category}"][f"{item}"] = new_limit
                except KeyError:
                    # 如果 item 不存在，新增一個新的 item
                    data["bag"][f"{category}"][f"{item}"] = limit
                with open(f"./database/users/{id}.json","w+",encoding='utf-8') as f:
                    json.dump(data,f)
        elif choice == "sell":
            if data["bag"] == {}: 
                embed = Embed(title=":x: | 你沒有物品可出售!",colour=Colour.red())
                await interaction.response.send_message(embed=embed,ephemeral=True)
            else:
                try:
                    # 如果 item 存在，更新 item 的 limit
                    new_limit = data["bag"][f"{category}"][f"{item}"] - limit
                    data["bag"][f"{category}"][f"{item}"] = new_limit
                    item_prices = {"diamond_ore":615,"gold_ore":500,"iron_ore":80,"coal":50,"stone":45}
                    price = item_prices.get(item)
                    total_price = price * limit
                    before = data["money"]
                    data["money"] = before + total_price
                    with open(f"./database/users/{id}.json","w",encoding='utf-8') as f:
                        json.dump(data,f)
                    embed = Embed(title=f"✅ | 你出售了 {item} x{limit}個! 獲得了`{total_price}`$",colour=Colour.green())
                    await interaction.response.send_message(embed=embed)
                except KeyError:
                    embed = Embed(title=":x: | 你沒有此物品可出售!",colour=Colour.red())
                    await interaction.response.send_message(embed=embed,ephemeral=True)
        elif choice == "give":
            if data["bag"] == {}: 
                embed = Embed(title=":x: | 你沒有物品可給予!",colour=Colour.red())
                await interaction.response.send_message(embed=embed,ephemeral=True)
            else:
                try:
                    pass
                except KeyError:
                    embed = Embed(title=":x: | 你沒有此物品可給予!",colour=Colour.red())
                    await interaction.response.send_message(embed=embed,ephemeral=True)
    except KeyError:
        await initialization(bot,interaction,id,object="nokey")
        await interaction.response.defer()
        data["bag"] = {f"{category}":{}}
        data["bag"][f"{category}"][f"{item}"] = limit
        with open(f"./database/users/{id}.json","w",encoding='utf-8') as f:
                json.dump(data,f)

async def translate(data, translation):
    if isinstance(data, dict):
        return {translation.get(k, k): await translate(v, translation) for k, v in data.items()}
    elif isinstance(data, list):
        return [await translate(i, translation) for i in data]
    else:
        return data

async def now_work(bot:Bot, interaction:Interaction,id:int):
    with open(f"./database/users/{id}.json","r",encoding="utf-8'") as f:
            data = json.load(f)
    stamina = data["stamina"]
    times = data["times"]
    try:
        new_stamina = stamina - random.randint(1,3)
        new_times = int(times) + 1
        data["times"] = new_times
        data["stamina"] = new_stamina
        with open(f"./database/users/{id}.json","w+",encoding='utf-8') as f:
                json.dump(data,f)
    except KeyError:
        await initialization(bot=bot, interaction=interaction, object="nokey")
        new_stamina = stamina - random.randint(1,3)
        new_times = int(times) + 1
        data["times"] = new_times
        data["stamina"] = new_stamina
        with open(f"./database/users/{id}.json","w+",encoding='utf-8') as f:
                json.dump(data,f)