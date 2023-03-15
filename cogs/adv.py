import disnake
from disnake.ext import commands
from disnake import ApplicationCommandInteraction,ButtonStyle
from PIL import Image
from PIL import ImageDraw,ImageFont
import numpy as np
class UI(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.monster = {
            "怪物":
            {
            "小兵":{
                "名稱":"Monster",
                "攻擊力":5,
                "生命值":10,
                "防禦值":1
                },
            "???":{
                "名稱":"???",
                "攻擊力":"?",
                "生命值":99999999,
                "防禦值":"?"
            }
            }
        }
        self.data = self.monster["怪物"]["???"]
        self.name = self.data["名稱"]
        self.attack_power = self.data["攻擊力"]
        self.health = self.data["生命值"]
        self.defense = self.data["防禦值"]

    @disnake.ui.button(label="攻擊",style=ButtonStyle.red)
    async def attack(self, button: disnake.ui.Button, interaction:ApplicationCommandInteraction):
        img = Image.open("box.png")
        img.save("box1.png")
        Deduct_heaalth = np.random.randint(1,5)
        self.health = self.health - np.random.randint(1,5) - Deduct_heaalth
        embed = disnake.Embed(title=f"你遇到了{self.name}!",description=f"你攻擊了他`{Deduct_heaalth}`滴血!\n怪物還剩`{self.health}`滴血",colour=disnake.Colour.random())
        file = disnake.File("box1.png", filename="image.png")
        embed.set_image(url="attachment://image.png")
        await interaction.response.edit_message(embed=embed,file=file)
    
    @disnake.ui.button(label="檢查",style=ButtonStyle.green)
    async def check(self, button: disnake.ui.Button, ApplicationCommandInteraction:ApplicationCommandInteraction):
        BattleBox(text=f"{self.name} {self.attack_power} ATK {self.defense} DEF", text1="Just Kill.",text2=None,color=(255,255,255),color1=(255,0,0),color2=None)
        embed = disnake.Embed(title=f"你遇到了{self.name}!",colour=disnake.Colour.random())
        file = disnake.File("box1.png", filename="image.png")
        embed.set_image(url="attachment://image.png")
        await ApplicationCommandInteraction.response.edit_message(embed=embed,file=file)

def BattleBox(text,text1,text2,color,color1,color2): #(255,255,255) White, (255,0,0) Red,(255,255,0) yellow 
    img = Image.open("box.png")
    font = ImageFont.truetype("determination_mono.ttf", 36)
    I2 = ImageDraw.Draw(img)
    if text != None:
        I2.text((28,30),f"* {text}",fill=color,font=font)
    if text1 != None:
        I2.text((28,70),f"* {text1}",fill=color1,font=font)
    if text2 != None:
        I2.text((28,110),f"* {text2}",fill=color2,font=font)
    img.save("box1.png")

class Adv(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        super().__init__()
        self.monster = {
            "怪物":
            {
            "小兵":{
                "名稱":"Monster",
                "攻擊力":5,
                "生命值":10,
                "防禦值":1
                },
            "???":{
                "名稱":"???",
                "攻擊力":"?",
                "生命值":99999999,
                "防禦值":"?"
            }
            }
        }
        self.data = self.monster["怪物"]["???"]
        self.name = self.data["名稱"]
        self.attack_power = self.data["攻擊力"]
        self.health = self.data["生命值"]
        self.defense = self.data["防禦值"]
    @commands.Cog.listener()
    async def on_ready(self):
        print("Adv Ready!")

    @commands.slash_command(name="冒險攻擊", description="攻擊敵人!",guild_ids=[1053616489128808499])
    async def advattack(self, interaction:ApplicationCommandInteraction):
        if interaction.user.id != 549056425943629825:
            view = UI()
            dialog_list = ["You got lost.","What just happened?","It's just a blocker.","It feels really bad.","Just Kill."]
            random_dialog = np.random.choice(dialog_list)
            BattleBox(text=f"{random_dialog}", text1=None,text2=None,color=(255,255,255),color1=None,color2=None)
            embed = disnake.Embed(title=f"你遇到了{self.name}!",colour=disnake.Colour.random())
            file = disnake.File("box1.png", filename="image.png")
            embed.set_image(url="attachment://image.png")
            await interaction.response.send_message(embed=embed,view=view,file=file)
        else:
            await interaction.response.send_message("冒險功能正在製作中!")
def setup(bot):
    bot.add_cog(Adv(bot))
