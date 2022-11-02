# -*- coding: utf-8 -*-
from discord.ext import commands


class Motd(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Message of the day ist bereit")

    @commands.group()
    async def motd(self, ctx: commands.Context):
        await ctx.reply("Ich bin noch nicht fertig...")


def setup(bot: commands.Bot):
    bot.add_cog(Motd(bot))
