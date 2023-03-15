import json
import requests

from os import getenv, listdir, path, mkdir, rename
from disnake import Game,Option,OptionType,ApplicationCommandInteraction
from disnake.abc import MISSING
from disnake.ext import commands
from disnake.ext.commands import Bot as OriginalBot
from lavalink import Client

from library.sources.source import SourceManager


class Bot(OriginalBot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.lavalink: Client = MISSING

        with open("configs/icons.json", "r", encoding="utf-8") as f:
            self.icons = json.load(f)


    async def on_ready(self):
        self.get_lavalink()
        self.__setup_lavalink_client()
        await self.change_presence(activity=Game(name="機器人版本:V1.1.1 | 作者by 鰻頭"))

    
    async def on_message(self, message):
        if message.content == '鰻頭':
            await message.channel.send("Maaaaaaaaan頭")

    def __setup_lavalink_client(self):
        """
        Sets up the lavalink client for the bot
        :return: Lavalink Client
        """
        self.lavalink = Client(self.user.id)

        with open("configs/lavalink.json", "r") as f:
            config = json.load(f)

        for node in config['nodes']:
            self.lavalink.add_node(**node)

        self.lavalink.register_source(SourceManager())

    def get_icon(self, name: str, default: any) -> any:
        """
        Get an icon
        :param name: The name of the icon
        :param default: The default value to return if the icon is not found
        :return: The icon
        """
        dct = self.icons.copy()

        for key in name.split("."):
            try:
                dct = dct[key]
            except KeyError:
                return default

        return dct
    
    def get_lavalink(self):
        print("Installing Lavalink...")

        if path.isfile("./lavalink/Lavalink.jar"):
            return

        if not path.isdir('./lavalink'):
            mkdir('./lavalink')

        data = requests.get("https://api.github.com/repos/freyacodes/Lavalink/releases/latest").json()

        jar = requests.get(data["assets"][0]["browser_download_url"])

        with open("./lavalink/Lavalink.jar", 'wb') as f:
            f.write(jar.content)
    
