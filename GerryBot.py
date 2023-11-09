import os
from os import sep
from dotenv import load_dotenv, set_key
from pathlib import Path
import asyncio
import discord
from discord import client
from discord import Client
from discord.ext import commands, tasks
import random
from discord.ext.commands.errors import MissingPermissions
from discord.gateway import WebSocketClosure
from discord import colour
from discord import channel
from discord.ext.commands import Bot

description = '''Gerry.'''

disctoke = input('Discord Token: ')

env_file_path = Path("DISCORD_TOKEN.env")
set_key(dotenv_path=env_file_path, key_to_set="DISCORD_TOKEN", value_to_set=disctoke)

load_dotenv(dotenv_path=env_file_path)

intents = discord.Intents.all()
intents.members = True
client = discord.Client(intents=intents)
TOKEN = os.getenv('DISCORD_TOKEN')


bot = commands.Bot(command_prefix='?', description=description, intents=intents)

async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await bot.load_extension(f"cogs.{filename[:-3]}")

@bot.command()
async def reload(ctx):
    await ctx.message.delete()
    await ctx.send('reloading')
    await bot.change_presence(activity=discord.Game(name='Reloading'))
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await bot.unload_extension(f"cogs.{filename[:-3]}")
    await ctx.send('unloading')
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await bot.load_extension(f"cogs.{filename[:-3]}")
    await ctx.send('loaded')
    await ctx.channel.purge(limit= 3)

intents = discord.Intents.all()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        timer = {round(error.retry_after, 2)}
        await ctx.send('Server start request already sent, you can send another in {0}seconds'.format(timer), delete_after=60.0)

@bot.event
async def on_message(message):
    # Checking if its a dm channel
    if isinstance(message.channel, discord.DMChannel):
        # Getting the channel
        if message.author.id == 810164134683082752:
            channel = bot.get_channel(862195419688861697)
            await channel.send(f"{message.author} sent:\n```{message.content}```")
        else:
            channel = bot.get_channel(862195419688861697)
            allowed_mentions = discord.AllowedMentions(everyone = True)
            await channel.send(f"@everyone {message.author} sent:\n```{message.content}```", allowed_mentions = allowed_mentions)
            answers = [
            "Ah sure there's a good chance of it",
            "The ra will support this",
            "Not in my 35 years have I seen that happening",
            "This is essential",
            "I believe you can achieve this",
            "This is a tremendous challenge, however not insurmountable",
            "You will have to plan and plan and plan again to deliver",
            "The foggy dew is clouding my judgement on this",
            "I can't reveal that",
            "I know nothing about that",
            "There is a higher chance of the queen dying",
            "The informants say no",
            "That will never happen in a law and order country"
            ]
            result = random.choice (answers)
            await message.author.send(result)
    # Processing the message so commands will work
    await bot.process_commands(message)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
        
async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)


asyncio.run(main())
