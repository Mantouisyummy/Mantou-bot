import disnake
from disnake.ext import commands
from disnake import ApplicationCommandInteraction, Option, Member
import datetime
import numpy as np
from numpy import random
from typing import Optional



class View(disnake.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
        self.choice = None
    
    @disnake.ui.button(label= "我接受!", style=disnake.ButtonStyle.green)
    async def agree(self, button: disnake.ui.Button, interaction: ApplicationCommandInteraction):
        if victim != str(interaction.user.id):
            embed = disnake.Embed(title=":x: | 你幹嘛自己點", colour=disnake.Colour.red())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.response.send_message(embed=embed, ephemeral=True)
        if victim == str(interaction.user.id):
            self.value = False
            self.choice = "agree"
            self.stop()

    @disnake.ui.button(label= "我拒絕!", style=disnake.ButtonStyle.red)
    async def deny(self, button: disnake.ui.Button, interaction: ApplicationCommandInteraction):
        if victim != str(interaction.user.id):
            embed = disnake.Embed(title=":x: | 你幹嘛自己點", colour=disnake.Colour.red())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.response.send_message(embed=embed, ephemeral=True)
        if victim == str(interaction.user.id):
            self.value = False
            self.choice = "deny"
            self.stop()
     
class AttackView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=0)
        self.value = None
        self.防禦 = None
        self.action = victim
        self.victim_hp = 20 #被攻擊者
        self.attacker_hp = 20 #攻擊者
        self.round = 1
    @disnake.ui.button(label= "攻擊他!", style=disnake.ButtonStyle.green, emoji="<:sword:1033263249988268094>")
    async def attack(self, button: disnake.ui.Button, interaction: ApplicationCommandInteraction):
        global victim_hp
        global attacker_hp
        victim_hp = self.victim_hp
        attacker_hp = self.attacker_hp
        action = self.action
        global Deduct_attacker_hp
        global Deduct_victim_hp
        battleemoji = disnake.utils.get(guild.emojis, name="sword2")
        emoji = disnake.utils.get(guild.emojis, name="sword")
        vsemoji = disnake.utils.get(guild.emojis, name="vs")
        shieldemoji = disnake.utils.get(guild.emojis, name="shield1")
        if self.action == victim and victim == str(interaction.user.id): #守方的攻擊 (對方防禦時)
            if self.防禦 == True:
                print("是我啦哈哈")
                Deducthp = random.randint(1,6) - Deductdef
                retaliation = random.choice(['成功','失敗']) #反傷
                if Deducthp < 0:
                    if retaliation == "失敗":
                        Deducthp = 0
                        print("被攻方的防禦值:" + str(Deductdef))
                        print("被攻方減少的hp:" + str(Deducthp))
                        Deduct_attacker_hp = self.attacker_hp - Deducthp
                        self.attacker_hp = Deduct_attacker_hp
                        print("攻擊方血量 " + str(attacker_hp))
                        embed = disnake.Embed(title="{0} | {1} 的攻擊!".format(battleemoji, interaction.user.name),description="你打了 <@{0}> `{1}` 滴血!!!".format(attacker, Deducthp), colour=disnake.Colour.red())
                        embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                        embed = disnake.Embed(title="{0} | 戰鬥開始 - 第{1}回合!".format(emoji, self.round), description="因對方使用了{8}盾牌防禦部分傷害，因此 {6} 打了 <@{0}> `{1}` 滴血!!!\n-------------------------------\n<@{2}> 的血為 `{3}`\n {7} \n<@{4}> 的血為 `{5}`\n-------------------------------".format(attacker, Deducthp, attacker, Deduct_attacker_hp, victim, victim_hp, interaction.user.mention, vsemoji, shieldemoji), colour=disnake.Colour.random())
                        embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                        await interaction.followup.edit_message(message_id=message_fetch.id ,embed=embed, view=self)
                        self.round = self.round + 1
                        self.action = attacker
                        action = self.action
                        self.value = False
                        self.防禦 = None
                    else:
                        Deducthp = 0
                        print("被攻方的防禦值:" + str(Deductdef))
                        print("被攻方減少的hp:" + str(Deducthp))
                        Deduct_attacker_hp = self.attacker_hp - Deducthp
                        retaliation_hp = random.randint(1,2)
                        self.attacker_hp = Deduct_attacker_hp
                        self.attacker_hp = self.attacker_hp - retaliation_hp
                        print("攻擊方血量 " + str(attacker_hp))
                        embed = disnake.Embed(title="{0} | {1} 的攻擊!".format(battleemoji, interaction.user.name),description="你打了 <@{0}> `{1}` 滴血!!!".format(attacker, Deducthp), colour=disnake.Colour.red())
                        embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                        embed = disnake.Embed(title="{0} | 戰鬥開始 - 第{1}回合!".format(emoji, self.round), description="因對方使用了{8}盾牌防禦部分傷害，因此 {6} 打了 <@{0}> `{1}` 滴血!!!\n-------------------------------\n<@{2}> 的血為 `{3}`\n {7} \n<@{4}> 的血為 `{5}`\n你突然遭到了反噬，你被扣了 `{9}` 滴血\n-------------------------------".format(attacker, Deducthp, attacker, Deduct_attacker_hp, victim, victim_hp, interaction.user.mention, vsemoji, shieldemoji,retaliation_hp), colour=disnake.Colour.random())
                        embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                        await interaction.followup.edit_message(message_id=message_fetch.id ,embed=embed, view=self)
                        self.round = self.round + 1
                        self.action = attacker
                        action = self.action
                        self.value = False
                        self.防禦 = None
                else:
                    if retaliation == "失敗":
                        print("被攻方的防禦值:" + str(Deductdef))
                        print("被攻方減少的hp:" + str(Deducthp))
                        Deduct_attacker_hp = self.attacker_hp - Deducthp
                        self.attacker_hp = Deduct_attacker_hp
                        print("攻擊方血量 " + str(attacker_hp))
                        embed = disnake.Embed(title="{0} | {1} 的攻擊!".format(battleemoji, interaction.user.name),description="你打了 <@{0}> `{1}` 滴血!!!".format(attacker, Deducthp), colour=disnake.Colour.red())
                        embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                        embed = disnake.Embed(title="{0} | 戰鬥開始 - 第{1}回合!".format(emoji, self.round), description="因對方使用了{8}盾牌防禦部分傷害，因此 {6} 打了 <@{0}> `{1}` 滴血!!!\n-------------------------------\n<@{2}> 的血為 `{3}`\n {7} \n<@{4}> 的血為 `{5}`\n-------------------------------".format(attacker, Deducthp, attacker, Deduct_attacker_hp, victim, victim_hp, interaction.user.mention, vsemoji, shieldemoji), colour=disnake.Colour.random())
                        embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                        await interaction.followup.edit_message(message_id=message_fetch.id ,embed=embed, view=self)
                        self.round = self.round + 1
                        self.action = attacker
                        action = self.action
                        self.value = False
                        self.防禦 = None
                    else:
                        Deducthp = 0
                        print("被攻方的防禦值:" + str(Deductdef))
                        print("被攻方減少的hp:" + str(Deducthp))
                        Deduct_attacker_hp = self.attacker_hp - Deducthp
                        retaliation_hp = random.randint(1,2)
                        self.attacker_hp = Deduct_attacker_hp
                        self.attacker_hp = self.attacker_hp - retaliation_hp
                        print("攻擊方血量 " + str(attacker_hp))
                        embed = disnake.Embed(title="{0} | {1} 的攻擊!".format(battleemoji, interaction.user.name),description="你打了 <@{0}> `{1}` 滴血!!!".format(attacker, Deducthp), colour=disnake.Colour.red())
                        embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                        embed = disnake.Embed(title="{0} | 戰鬥開始 - 第{1}回合!".format(emoji, self.round), description="因對方使用了{8}盾牌防禦部分傷害，因此 {6} 打了 <@{0}> `{1}` 滴血!!!\n-------------------------------\n<@{2}> 的血為 `{3}`\n {7} \n<@{4}> 的血為 `{5}`\n你突然遭到了反噬，你被扣了 `{9}` 滴血\n-------------------------------".format(attacker, Deducthp, attacker, Deduct_attacker_hp, victim, victim_hp, interaction.user.mention, vsemoji, shieldemoji,retaliation_hp), colour=disnake.Colour.random())
                        embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                        await interaction.followup.edit_message(message_id=message_fetch.id ,embed=embed, view=self)
                        self.round = self.round + 1
                        self.action = attacker
                        action = self.action
                        self.value = False
                        self.防禦 = None
            elif self.防禦 == None or False:
                print(self.action)
                Deducthp = random.randint(1,5)
                Deduct_attacker_hp = self.attacker_hp - Deducthp
                self.attacker_hp = Deduct_attacker_hp
                print("攻擊方血量 " + str(attacker_hp))
                embed = disnake.Embed(title="{0} | {1} 的攻擊!".format(battleemoji, interaction.user.name),description="你打了 <@{0}> `{1}` 滴血!!!".format(attacker, Deducthp), colour=disnake.Colour.red())
                embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                await interaction.response.send_message(embed=embed, ephemeral=True)
                embed = disnake.Embed(title="{0} | 戰鬥開始 - 第{1}回合!".format(emoji, self.round), description="{6} 打了 <@{0}> `{1}` 滴血!!!\n-------------------------------\n<@{2}> 的血為 `{3}`\n {7} \n<@{4}> 的血為 `{5}`\n-------------------------------".format(attacker, Deducthp, attacker, Deduct_attacker_hp, victim, victim_hp, interaction.user.mention, vsemoji), colour=disnake.Colour.random())
                embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                await interaction.followup.edit_message(message_id=message_fetch.id ,embed=embed, view=self)
                self.round = self.round + 1
                self.value = False
                self.action = attacker
                action = self.action
            elif self.action == victim and victim != str(interaction.user.id):
                print("攻擊時round:" + self.action)
                print("else被攻擊的人:" + str(interaction.user.id))
                embed = disnake.Embed(title=":x: | 還沒到你的回合", colour=disnake.Colour.red())
                embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                await interaction.response.send_message(embed=embed, ephemeral=True)
                pass

        if self.action == attacker and attacker == str(interaction.user.id): #攻方的攻擊 (對方防禦時)
            if self.防禦 == True: 
                print("是我啦ㄏ哈")
                self.action = victim
                Deducthp = (random.randint(1,6)) - Deductdef     
                retaliation = random.choice(['成功','失敗']) #反傷
                if Deducthp < 0:
                    if retaliation == "失敗":
                        Deducthp = 0
                        print("攻方的防禦值:" + str(Deductdef))
                        print("攻方減少的hp:" + str(Deducthp))
                        Deduct_victim_hp = self.victim_hp - Deducthp
                        self.victim_hp = Deduct_victim_hp
                        embed = disnake.Embed(title="{0} | {1} 的攻擊!".format(battleemoji, interaction.user.name),description="你打了 <@{0}> `{1}` 滴血!!!".format(victim, Deducthp), colour=disnake.Colour.red())
                        embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                        infoembed = disnake.Embed(title="{0} | 戰鬥開始 - 第{1}回合!".format(emoji, self.round), description="因對方使用了{8}盾牌防禦部分傷害，因此 {6} 打了 <@{0}> `{1}` 滴血!!!\n-------------------------------\n<@{2}> 的血為 `{3}`\n {7} \n<@{4}> 的血為 `{5}`\n-------------------------------".format(victim, Deducthp, attacker, Deduct_attacker_hp, victim, Deduct_victim_hp, interaction.user.mention, vsemoji, shieldemoji), colour=disnake.Colour.random())
                        embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                        await interaction.followup.edit_message(message_id=message_fetch.id ,embed=infoembed, view=self)
                        self.round = self.round + 1
                        self.防禦 = None
                        self.value = False
                    else:
                        Deducthp = 0
                        print("攻方的防禦值:" + str(Deductdef))
                        print("攻方減少的hp:" + str(Deducthp))
                        Deduct_victim_hp = self.victim_hp - Deducthp
                        self.victim_hp = Deduct_victim_hp
                        retaliation_hp = random.randint(1,2)
                        self.victim_hp = self.victim_hp - retaliation_hp
                        embed = disnake.Embed(title="{0} | {1} 的攻擊!".format(battleemoji, interaction.user.name),description="你打了 <@{0}> `{1}` 滴血!!!".format(victim, Deducthp), colour=disnake.Colour.red())
                        embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                        infoembed = disnake.Embed(title="{0} | 戰鬥開始 - 第{1}回合!".format(emoji, self.round), description="對方使用了{8}盾牌防禦部分傷害，因此 {6} 打了 <@{0}> `{1}` 滴血!!!\n你突然遭到了反噬，你被扣了 `{9}` 滴血\n-------------------------------\n<@{2}> 的血為 `{3}`\n {7} \n<@{4}> 的血為 `{5}`\n-------------------------------".format(victim, Deducthp, attacker, Deduct_attacker_hp, victim, Deduct_victim_hp, interaction.user.mention, vsemoji, shieldemoji,retaliation_hp), colour=disnake.Colour.random())
                        embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                        await interaction.followup.edit_message(message_id=message_fetch.id ,embed=infoembed, view=self)
                        self.round = self.round + 1
                        self.防禦 = None
                        self.value = False
                else:
                    if retaliation == "失敗":
                        print("攻方的防禦值:" + str(Deductdef))
                        print("攻方減少的hp:" + str(Deducthp))
                        Deduct_victim_hp = self.victim_hp - Deducthp
                        self.victim_hp = Deduct_victim_hp
                        embed = disnake.Embed(title="{0} | {1} 的攻擊!".format(battleemoji, interaction.user.name),description="你打了 <@{0}> `{1}` 滴血!!!".format(victim, Deducthp), colour=disnake.Colour.red())
                        embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                        infoembed = disnake.Embed(title="{0} | 戰鬥開始 - 第{1}回合!".format(emoji, self.round), description="因對方使用了{8}盾牌防禦部分傷害，因此 {6} 打了 <@{0}> `{1}` 滴血!!!\n-------------------------------\n<@{2}> 的血為 `{3}`\n {7} \n<@{4}> 的血為 `{5}`\n-------------------------------".format(victim, Deducthp, attacker, Deduct_attacker_hp, victim, Deduct_victim_hp, interaction.user.mention, vsemoji, shieldemoji), colour=disnake.Colour.random())
                        embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                        await interaction.followup.edit_message(message_id=message_fetch.id ,embed=infoembed, view=self)
                        self.round = self.round + 1
                        self.防禦 = None
                        self.value = False
                    else:
                        Deducthp = 0
                        print("攻方的防禦值:" + str(Deductdef))
                        print("攻方減少的hp:" + str(Deducthp))
                        Deduct_victim_hp = self.victim_hp - Deducthp
                        self.victim_hp = Deduct_victim_hp
                        retaliation_hp = random.randint(1,2)
                        self.victim_hp = self.victim_hp - retaliation_hp
                        embed = disnake.Embed(title="{0} | {1} 的攻擊!".format(battleemoji, interaction.user.name),description="你打了 <@{0}> `{1}` 滴血!!!".format(victim, Deducthp), colour=disnake.Colour.red())
                        embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                        infoembed = disnake.Embed(title="{0} | 戰鬥開始 - 第{1}回合!".format(emoji, self.round), description="對方使用了{8}盾牌防禦部分傷害，因此 {6} 打了 <@{0}> `{1}` 滴血!!!\n你突然遭到了反噬，你被扣了 `{9}` 滴血\n-------------------------------\n<@{2}> 的血為 `{3}`\n {7} \n<@{4}> 的血為 `{5}`\n-------------------------------".format(victim, Deducthp, attacker, Deduct_attacker_hp, victim, Deduct_victim_hp, interaction.user.mention, vsemoji, shieldemoji,retaliation_hp), colour=disnake.Colour.random())
                        embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                        await interaction.followup.edit_message(message_id=message_fetch.id ,embed=infoembed, view=self)
                        self.round = self.round + 1
                        self.防禦 = None
                        self.value = False

            elif self.防禦 == None or False:
                self.action = victim
                Deducthp = random.randint(1,5)
                Deduct_victim_hp = self.victim_hp - Deducthp
                self.victim_hp = Deduct_victim_hp
                print("被攻擊方血量 " + str(victim_hp))
                embed = disnake.Embed(title="{0} | {1} 的攻擊!".format(battleemoji, interaction.user.name),description="你打了 <@{0}> `{1}` 滴血!!!".format(victim, Deducthp), colour=disnake.Colour.red())
                embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                await interaction.response.send_message(embed=embed, ephemeral=True)
                infoembed = disnake.Embed(title="{0} | 戰鬥開始 - 第{1}回合!".format(emoji, self.round), description="{6}打了 <@{0}> `{1}` 滴血!!!\n-------------------------------\n<@{2}> 的血為 `{3}`\n {7} \n<@{4}> 的血為 `{5}`\n-------------------------------".format(victim, Deducthp, attacker, Deduct_attacker_hp, victim, Deduct_victim_hp, interaction.user.mention, vsemoji), colour=disnake.Colour.random())
                infoembed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                await interaction.followup.edit_message(message_id=message_fetch.id ,embed=infoembed, view=self)
                self.round = self.round + 1
                self.value = False
        elif self.action == attacker and attacker != str(interaction.user.id):
            try:
                print("攻擊時round:" + self.action)
                print("else被攻擊的人:" + str(interaction.user.id))
                embed = disnake.Embed(title=":x: | 還沒到你的回合", colour=disnake.Colour.red())
                embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                await interaction.response.send_message(embed=embed, ephemeral=True)
                pass
            except disnake.errors.InteractionResponded:
                pass
            
        if self.attacker_hp <= 0:
            inte = int("FFA500", 16)
            color = hex(inte)
            trophyemoji = disnake.utils.get(guild.emojis, name="trophy")
            view = OverView()
            print("遊戲結束!")
            embed = disnake.Embed(title="{} | 遊戲結束!".format(trophyemoji),description="恭喜 {} 勝利!!!!!!!!!".format(interaction.user.name), colour=int(color, 16))
            await interaction.followup.edit_message(message_id=message_fetch.id ,embed=embed, view=view)
        elif self.victim_hp <=0:
            inte = int("FFA500", 16)
            color = hex(inte)
            trophyemoji = disnake.utils.get(guild.emojis, name="trophy")
            view = OverView()
            print("遊戲結束!")
            embed = disnake.Embed(title="{} | 遊戲結束!".format(trophyemoji),description="恭喜 {} 勝利!!!!!!!!!".format(interaction.user.name), colour=int(color,16))
            await interaction.followup.edit_message(message_id=message_fetch.id ,embed=embed, view=view)

    @disnake.ui.button(label= "防禦", style=disnake.ButtonStyle.gray,emoji="<:shield1:1033672396353314856>")
    async def deftense(self, button: disnake.ui.Button, interaction: ApplicationCommandInteraction):
        victim_hp = self.victim_hp
        attacker_hp = self.attacker_hp
        action = self.action
        global Deductdef
        Deductdef = random.randint(2,5)
        shieldemoji = disnake.utils.get(guild.emojis, name="shield1")
        emoji = disnake.utils.get(guild.emojis, name="sword")
        vsemoji = disnake.utils.get(guild.emojis, name="vs")
        if self.action == victim and victim == str(interaction.user.id):
            Deduct_victim_hp = self.victim_hp
            embed = disnake.Embed(title="{0} | 狀態報告".format(shieldemoji),description="你使出了防禦! 對方攻擊你的傷害降低了!", colour=disnake.Colour.red())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            embed = disnake.Embed(title="{0} | 戰鬥開始 - 第{1}回合!".format(emoji, self.round), description="{0} 這回合使用了防禦!\n-------------------------------\n<@{1}> 的血為 `{2}`\n {3} \n<@{4}> 的血為 `{5}`\n-------------------------------".format(interaction.user.mention, attacker, self.attacker_hp, vsemoji, victim, Deduct_victim_hp), colour=disnake.Colour.random())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.followup.edit_message(message_id=message_fetch.id ,embed=embed, view=self)
            self.round = self.round + 1
            self.value = False
            self.防禦 = True
            self.action = attacker
            action = self.action
        elif self.action == victim and victim != str(interaction.user.id):
            print("else被攻擊的人:" + str(interaction.user.id))
            embed = disnake.Embed(title=":x: | 還沒到你的回合", colour=disnake.Colour.red())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            pass
        if self.action == attacker and attacker == str(interaction.user.id):
            print("攻擊時round:" + self.action)
            print("攻擊時:" + str(interaction.user.id))
            Deduct_victim_hp = self.victim_hp
            Deduct_attacker_hp = self.attacker_hp
            print("被攻擊方血量 " + str(victim_hp))
            embed = disnake.Embed(title="{0} | 狀態報告".format(shieldemoji),description="你使出了防禦! 對方攻擊你的傷害降低了!", colour=disnake.Colour.red())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            infoembed = disnake.Embed(title="{0} | 戰鬥開始 - 第{1}回合!".format(emoji, self.round), description="{0} 這回合使用了防禦!\n-------------------------------\n<@{1}> 的血為 `{2}`\n {3} \n<@{4}> 的血為 `{5}`\n-------------------------------".format(interaction.user.mention, attacker, self.attacker_hp, vsemoji, victim, Deduct_victim_hp), colour=disnake.Colour.random())
            infoembed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.followup.edit_message(message_id=message_fetch.id ,embed=infoembed, view=self)
            self.round = self.round + 1
            self.value = False
            self.防禦 = True
            self.action = victim
            action = self.action
        elif self.action == attacker and attacker != str(interaction.user.id):
            try:
                print("else攻擊時round:" + self.action)
                print("else攻擊時:" + str(interaction.user.id))
                embed = disnake.Embed(title=":x: | 還沒到你的回合", colour=disnake.Colour.red())
                embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                await interaction.response.send_message(embed=embed, ephemeral=True)
                pass
            except disnake.errors.InteractionResponded:
                pass
        if self.attacker_hp <= 0:
            inte = int("FFA500", 16)
            color = hex(inte)
            trophyemoji = disnake.utils.get(guild.emojis, name="trophy")
            view = OverView()
            print("遊戲結束!")
            embed = disnake.Embed(title="{} | 遊戲結束!".format(trophyemoji),description="恭喜 <@{}> 勝利!!!!!!!!!".format(victim), colour=int(color, 16))
            await interaction.followup.edit_message(message_id=message_fetch.id ,embed=embed, view=view)
        elif self.victim_hp <=0:
            inte = int("FFA500", 16)
            color = hex(inte)
            trophyemoji = disnake.utils.get(guild.emojis, name="trophy")
            view = OverView()
            print("遊戲結束!")
            embed = disnake.Embed(title="{} | 遊戲結束!".format(trophyemoji),description="恭喜 {} 勝利!!!!!!!!!".format(attacker), colour=int(color,16))
            await interaction.followup.edit_message(message_id=message_fetch.id ,embed=embed, view=view)
    
    @disnake.ui.button(label="🪄技能釋放", style=disnake.ButtonStyle.blurple)
    async def skill(self, button: disnake.ui.Button, interaction: ApplicationCommandInteraction):
        emoji = disnake.utils.get(guild.emojis, name="sword")
        vsemoji = disnake.utils.get(guild.emojis, name="vs")
        if action == victim and victim == str(interaction.user.id): #守方的行動
            view = SkillView()
            embed = disnake.Embed(title="你準備使用技能!",description="請使用選單選擇一項技能", colour=disnake.Colour.green())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
            embed = disnake.Embed(title="{0} | 戰鬥開始 - 第{1}回合!".format(emoji, round), description="{0} 正在選擇技能...<a:Loading:1059806500241027157>\n-------------------------------\n<@{1}> 的血為 `{2}`\n {5} \n<@{3}> 的血為 `{4}`\n-------------------------------".format(interaction.user.mention,attacker, attacker_hp, victim, victim_hp, vsemoji), colour=disnake.Colour.random())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.followup.edit_message(message_id=message_fetch.id ,embed=embed, view=self)
        elif action == victim and victim != str(interaction.user.id):
            print("攻擊時round:" + action)
            print("else被攻擊的人:" + str(interaction.user.id))
            embed = disnake.Embed(title=":x: | 還沒到你的回合", colour=disnake.Colour.red())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            pass
        if action == attacker and attacker == str(interaction.user.id): #攻方的行動 
            view = SkillView()
            embed = disnake.Embed(title="你準備使用技能!",description="請使用選單選擇一項技能", colour=disnake.Colour.green())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            infoembed = disnake.Embed(title="{0} | 戰鬥開始 - 第{1}回合!".format(emoji, round), description="{0} 正在選擇技能...<a:Loading:1059806500241027157>\n-------------------------------\n<@{1}> 的血為 `{2}`\n {5} \n<@{3}> 的血為 `{4}`\n-------------------------------".format(interaction.user.mention, attacker, attacker_hp, victim, victim_hp, vsemoji), colour=disnake.Colour.random())
            infoembed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.followup.edit_message(message_id=message_fetch.id ,embed=infoembed, view=self)

class SkillView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(MagicDropdown())

class MagicDropdown(disnake.ui.Select):
    def __init__(self):
        self.skill_dict = [{"name":"麻吉炸彈","damage":3}]
        options = []
        for i in self.skill_dict:
            option = disnake.SelectOption(label=i["name"],value=i["name"])
            options.append(option)
            super().__init__(placeholder='選擇一個技能', min_values=1,max_values=1, options=options)
        
    async def callback(self, interaction: ApplicationCommandInteraction):
        emoji = disnake.utils.get(guild.emojis, name="sword")
        vsemoji = disnake.utils.get(guild.emojis, name="vs")
        if action == attacker and attacker == str(interaction.user.id): #攻方的技能釋放
            if self.values[0] == "麻吉炸彈":
                Deduct_victim_hp = victim_hp - 3
                await interaction.response.send_message(f"你使用了 {self.values[0]}",ephemeral=True)
                infoembed = disnake.Embed(title="{0} | 戰鬥開始 - 第{1}回合!".format(emoji, round), description=f"{interaction.user.mention} 使用了技能 {self.values[0]}!\n<@{victim}> 受到了`3`點傷害\n-------------------------------\n<<@{attacker}> 的血為 `{attacker_hp}`\n {vsemoji} \n<@{victim}> 的血為 `{Deduct_victim_hp}`\n-------------------------------",colour=disnake.Colour.random())
                infoembed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                view = AttackView()
                await interaction.followup.edit_message(message_id=message_fetch.id ,embed=infoembed, view=view)
        elif action == victim and victim == str(interaction.user.id): #守方的技能釋放
            if self.values[0] == "麻吉炸彈":
                Deduct_attacker_hp = attacker_hp - 3
                await interaction.response.send_message(f"你使用了 {self.values[0]}",ephemeral=True)
                infoembed = disnake.Embed(title="{0} | 戰鬥開始 - 第{1}回合!".format(emoji, round), description=f"{interaction.user.mention} 使用了技能 {self.values[0]}!\n<@{attacker}> 受到了`3`點傷害\n-------------------------------\n<@{attacker}> 的血為 `{Deduct_attacker_hp}`\n {vsemoji} \n<@{victim}> 的血為 `{victim_hp}`\n-------------------------------", colour=disnake.Colour.random())
                view = AttackView()
                infoembed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                await interaction.followup.edit_message(message_id=message_fetch.id ,embed=infoembed, view=view)
        

class OverView(disnake.ui.View):
    def __init__(self):
        super().__init__()
    

class fight(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Fight Ready!")
    
    @commands.slash_command(name='attack', description="攻擊你的朋友!",name_localizations={"zh-TW":"攻擊朋友"})
    async def attack(self, interaction: ApplicationCommandInteraction, user:Optional[Member] = Option(name="user", description="你要攻擊的朋友! 沒有朋友就算了",required=True)):
        global guild
        global action
        guild = self.bot.get_guild(1003837176464810115)
        emoji = disnake.utils.get(guild.emojis, name="sword")
        global victim
        global attacker
        global viewround
        attacker = str(interaction.user.id)
        str1 = str(user.id).strip("<")
        str2 = str1.strip(">")
        victim = str2.strip("@")
        print(victim)
        view = View()
        if victim == str(interaction.user.id):
            print("點的人:" + str(attacker))
            print("被攻擊的人:" + victim)
            embed = disnake.Embed(title=":x: | 你不能自己找自己當對手", colour=disnake.Colour.red())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        else:
            embed = disnake.Embed(title=":warning: 對決!", description="{} 想跟你對戰!".format(interaction.user.mention), colour=disnake.Colour.random())
            message = await interaction.response.send_message("{}".format(user.mention) ,embed=embed, view=view)
            global message_fetch
            message_fetch = await message.fetch()
            print("元訊息id: "+ str(message_fetch.id))
            await view.wait()

        if view.value is None:
            return

        if view.choice == "agree":
            global victim_hp
            global attacker_hp
            global round
            viewround = victim
            victim_hp = 30 #被攻擊者
            attacker_hp = 30 #攻擊者
            action = victim
            round = 1
            embed = disnake.Embed(title="{} | 戰鬥開始!".format(emoji), description="{0} 的血為 `{1}`\n vs \n{2} 的血為 `{3}`".format(interaction.user.mention, attacker_hp, user.mention, victim_hp), colour=disnake.Colour.random())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            attackview = AttackView()
            await interaction.edit_original_message(content=None,embed=embed, view=attackview)
               

        if view.choice == "deny":
            embed = disnake.Embed(title=":x: 他不跟你打", colour=disnake.Colour.red())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.edit_original_message(content=None ,embed=embed, view=None)




def setup(bot):
    bot.add_cog(fight(bot))
