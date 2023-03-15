import disnake
from disnake.ext import commands
from disnake import ApplicationCommandInteraction,Option
import random
class View(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        for i in get_role:
            print(i)
            self.add_item(disnake.ui.Button(label=f"{i}",custom_id=f"{i}"))
        

    
class DropdownView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(Dropdown())

class Dropdown(disnake.ui.Select):
  def __init__(self):
    options = []
    role_list = []
    role_dict = {}
    for i in list(role):
      role_dict["name"] = i.name
      role_dict["id"] = i.id
      role_list.append(role_dict.copy()) 
    for v in role_list:
        if not v["name"] is None:
            option = disnake.SelectOption(label='{}'.format(v["name"]),value="{}".format(v["id"]))
            options.append(option)
    super().__init__(placeholder='選擇要領取的身分組', min_values=1,max_values=5, options=options)
    
  async def callback(self,interaction: ApplicationCommandInteraction):
    global get_role
    get_role = []
    for i in self.values:
        role = disnake.utils.get(interaction.guild.roles,id=int(i))
        get_role.append(role.name)
    view = View()
    await message.edit(content=f"{global_text}",view=view,embed=None)


class GetRole(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        super().__init__()
    @commands.Cog.listener()
    async def on_ready(self):
        print("Get role Ready!")

    @commands.slash_command(name="role", description="透過一則訊息即可領取你要的身分組",name_localizations={"zh-TW":"領取身分"},guild_ids=[1053616489128808499])
    async def role(self, interaction: ApplicationCommandInteraction,text:str = Option(name="內文",description="訊息內文")):
        global role
        global message
        global global_text
        global_text = text
        role = interaction.guild.roles
        dropdownview = DropdownView()
        embed = disnake.Embed(title="請選擇要給別人領取的身分組",colour=disnake.Colour.random())
        temp = await interaction.response.send_message("加載中..",ephemeral=True)
        message = await interaction.channel.send(embed=embed,view=dropdownview)
        await temp.delete()
        

def setup(bot):
    bot.add_cog(GetRole(bot))