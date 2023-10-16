import discord
from discord import client
from discord.ext import commands, tasks
from discord.ext.commands import bot

client = discord.Client(intents = discord.Intents.all())

class Kneecap(commands.Cog):
    def __init__(self, bot):
        self.index = 0
        self.bot = bot
    
    @commands.command()
    async def kneecap(self, ctx, member : discord.Member):
        author = ctx.message.author
        ment = member.mention
        botUser = '@GerryBot#6844'
        print(member)
        await ctx.message.delete()
        if author == member:
            await ctx.send(ctx.message.author.mention + " You can't kneecap yourself!")
        if author == botUser:
            await ctx.send("Kneecaps {0}".format(ment))
        if author != member and author != botUser:
            await ctx.send("Kneecaps {0}".format(ment))

async def setup(bot):
    await bot.add_cog(Kneecap(bot))
    print('[KC] I am being loaded!')
async def teardown(bot):
    print('[KC] I am being unloaded!')