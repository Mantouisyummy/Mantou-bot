import disnake
import time
from disnake.ext import commands
from disnake import ApplicationCommandInteraction,TextInputStyle,ModalInteraction
from disnake import SelectOption
from disnake import Forbidden
import requests
import datetime


class Modal(disnake.ui.Modal):

  def __init__(self):
    components = [
    disnake.ui.TextInput(
      label="身分組名稱",
      placeholder="身分組的名稱",
      custom_id = "rolename",
      style=TextInputStyle.short,
      min_length=1,
      max_length=50,
    ),
    disnake.ui.TextInput(
      label="顏色 (使用顏色代碼,不用加#)",
      placeholder="#ffffff",
      custom_id = "color",
      style=TextInputStyle.short,
      min_length=6,
      max_length=6,
    ),
  ]
    super().__init__(title="自訂義身分組",components=components)


  async def callback(self, interaction: ModalInteraction):
    for key, value in interaction.text_values.items():
      colorcode = value
      rolename = key
    guild = interaction.guild
    num_roles = interaction.user.top_role.position
    inte = int(colorcode, 16)
    color = hex(inte)
    try:
      await guild.create_role(name=f"{rolename}",
                              colour=int(color, 16))
      role = disnake.utils.get(guild.roles, name=f"{rolename}")
      await role.edit(position=num_roles + 1)
      await interaction.user.add_roles(role)
      embed = disnake.Embed(title=":white_check_mark: 執行成功! ",
                           description=f"你已成功取得了 <@&{role.id}> 的身分組!",
                           color=disnake.Colour.random(),
                           timestamp=datetime.datetime.utcnow())
      await interaction.response.send_message(embed=embed, ephemeral=True)
    except disnake.HTTPException:
      await role.delete(reason="因錯誤而刪除!")
      await interaction.response.send_message("我沒有權限移動身分組!",ephemeral=True)



class View(disnake.ui.View):

  def __init__(self):
    super().__init__(timeout=None)

  @disnake.ui.button(label="設定", emoji="🔧", style=disnake.ButtonStyle.gray, custom_id="settings")
  async def set(self, button: disnake.ui.Button, interaction: ApplicationCommandInteraction):
    modal = Modal()
    await interaction.response.send_modal(modal=modal)


class autorole(commands.Cog):
  def __init__(self, bot:commands.Bot):
    self.bot = bot
  
  @commands.Cog.listener()
  async def on_ready(self):
    self.bot.add_view(View())
    print("Autorole Ready!")

  @commands.slash_command(name='customrole',description="自定義身分組",name_localizations={"zh-TW":"自訂身分組"})
  @commands.has_permissions(manage_roles=True)
  async def customrole(self, interaction: ApplicationCommandInteraction):
  
    embed = disnake.Embed(title="設置你專屬的身分組",
                           description="點選以下的按鈕來設定ㄅ",
                           color=disnake.Colour.random(),
                           timestamp=datetime.datetime.utcnow())
    view = View()
    await interaction.response.send_message(embed=embed, view=view)


def setup(bot):
  bot.add_cog(autorole(bot))
