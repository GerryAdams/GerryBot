import discord
from discord.channel import VoiceChannel
from discord.ext import commands
from discord.ext.commands.bot import Bot
import os
import asyncio
from discord.client import VoiceClient
import glob

client = commands.Bot(command_prefix="?")
songs = asyncio.Queue()
play_next_song = asyncio.Event()

class MusicBot(commands.Cog):
    def __init__(self, bot):
        self.index = 0
        self.bot = bot

    @commands.command()
    async def leave(context):
        await context.voice_client.disconnect()


    @commands.command()
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        print('Connected: ' + channel.name)
        print('Connected by: ' + ctx.message.author.name)
        await channel.connect()

    @commands.command()
    async def pause(ctx):
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
        else:
            await ctx.send("Nothing is currently playing.")

    @commands.command()
    async def resume(ctx):
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
        else:
            await ctx.send("The audio is not paused.")

    @commands.command()
    async def stop(ctx):
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        voice.stop()

def setup(bot):
    bot.add_cog(MusicBot(bot))
    print('[MusicB] I am being loaded!')
def teardown(bot):
    print('[MusicB] I am being unloaded!')