import asyncio
import json
import logging
from os import getenv
import os
from dotenv import load_dotenv

from disnake import Intents,Game
from disnake.ext.commands import CommandSyncFlags

from core.classes import Bot

logging.basicConfig(level=logging.INFO)


def main():
    loop = asyncio.new_event_loop()

    bot = Bot(
        command_prefix=getenv("PREFIX", "l!"), intents=Intents.all(), loop=loop,
        command_sync_flags=CommandSyncFlags.default()
    )

    load_extensions(bot)
    os.environ["SPOTIFY_CLIENT_ID"] = "b0b78f9873194e11b1841de3ec4eaeb7"
    os.environ["SPOTIFY_CLIENT_SECRET"] = "b838fc70282b44be8f29e395d14a4877"
    os.environ["SPOTIPY_REDIRECT_URI"] = "https://github.com/Mantou-9487"
    load_dotenv()
    token = os.getenv("TOKEN")
    bot.run(token)




def load_extensions(bot: Bot) -> Bot:
    """
    Load extensions in extensions.json file
    :param bot: The bot to load the extensions to
    :return: The bot
    """
    for fn in os.listdir("./cogs"):
        if fn.endswith(".py"):
            bot.load_extension(f"cogs.{fn[:-3]}")
    
    for fn in os.listdir("./cogs/music"):
        if fn.endswith(".py"):
            bot.load_extension(f"cogs.music.{fn[:-3]}")
    
    for fn in os.listdir("./cogs/rpg"):
        if fn.endswith(".py"):
            bot.load_extension(f"cogs.rpg.{fn[:-3]}")
    
    return bot

if __name__ == "__main__":
    main()
