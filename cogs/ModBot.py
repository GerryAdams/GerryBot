import discord
from discord import client
from discord.activity import CustomActivity
from discord.ext import commands, tasks
import random
from discord import Colour, message
from discord.ext.commands import Bot
from discord.utils import get
import asyncio
import time

client = discord.Client(intents = discord.Intents.all())

class ModBot(commands.Cog):
    def __init__(self, bot):
        self.index = 0
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def purge(self, ctx, amount : int):

        if amount > 50:
            amount = 50
            await ctx.channel.purge(limit= amount)
            print('{} purging {}'.format(ctx.message.author, amount))
        else:
            await ctx.channel.purge(limit= amount + 1)
            print('{} purging {}'.format(ctx.message.author, amount))
    
    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You need Administrator permissions to use this command!")



async def setup(bot):
    await bot.add_cog(ModBot(bot))
    print('[MB] I am being loaded!')
async def teardown(bot):
    print('[MB] I am being unloaded!')