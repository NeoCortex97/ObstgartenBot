# -*- coding: utf-8 -*-
import pathlib

import discord
from config import Settings
from discord.ext import commands


conf = Settings()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or(":"), intents=intents)

for path in pathlib.Path(__file__).parent.joinpath("cogs").iterdir():
    if not path.stem.startswith("__"):
        print(f'Lade {path.stem}')
        bot.load_extension(f'cogs.{path.stem}')


@bot.event
async def on_ready():
    print(f'Ich hab mich als {bot.user}')
    print(f'Du kannst mich unter dem Folgenden Link beitreten lassen:\n{conf.join_link}')
    for guild in bot.guilds:
        print(guild.name)


if __name__ == '__main__':
    bot.run(conf.bot_secret)
