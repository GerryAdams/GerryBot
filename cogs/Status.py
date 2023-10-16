import discord
from discord import client
from discord.activity import CustomActivity
from discord.ext import commands, tasks
import random
from discord import Colour, message
from discord.ext.commands.bot import Bot


client = discord.Client(intents = discord.Intents.all())

class Status(commands.Cog):
    def __init__(self, bot):
        self.index = 0
        self.bot = bot

    @commands.command()
    async def statusplay(ctx, *GameName:str):
        await client.change_presence(activity=discord.Game(name=' '.join(GameName)))
        print("Playing "+' '.join(GameName))
        print(ctx.message.author)
        print(ctx.message.author.id)

    @commands.command()
    async def statusstream(ctx, *StreamName:str):
        await client.change_presence(activity=discord.Streaming(name=' '.join(StreamName), url="https://www.youtube.com/watch?v=PWAkzuINxxQ"))
        print("Streaming "+' '.join(StreamName))

    @commands.command()
    async def statussong(ctx, *SongName:str):
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=' '.join(SongName)))
        print("Listening to "+' '.join(SongName))

    @commands.command()
    async def statuswatch(ctx, *ShowName:str):
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=' '.join(ShowName)))
        print("Watching "+' '.join(ShowName))


async def setup(bot):
    await bot.add_cog(Status(bot))
    print('[Status] I am being loaded!')
async def teardown(bot):
    print('[Status] I am being unloaded!')
