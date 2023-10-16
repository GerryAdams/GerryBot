import discord
from discord import client
from discord.activity import CustomActivity
from discord.ext import commands, tasks
import random
from discord import Colour, message
from discord.ext.commands.bot import Bot

client = discord.Client(intents = discord.Intents.all())

class VoteBot(commands.Cog):
    def __init__(self, bot):
        self.index = 0
        self.bot = bot
    
    global poll_messageID
    global comp
    global custom
    global msgauthor

    @commands.command(pass_context=True)
    async def quickpoll(self, ctx, *options: str):
        global embed_test
        await ctx.message.delete()
        if len(options) <= 1:
            await ctx.send('You need more than one option to make a poll!')
            return
        if len(options) > 10:
            await ctx.send('You cannot make a poll for more than 10 things!')
            return

        if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
            reactions = ['✅', '❌']
        else:
            reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
        embed_test = discord.Embed(title="Poll", description=''.join(description))
        poll = await ctx.send(embed=embed_test)
        
        for reaction in reactions[:len(options)]:
            await poll.add_reaction(reaction)
        embed_test.set_footer(text='Poll ID: {}'.format(poll.id))
        await ctx.edit_message(poll, embed=embed_test)

    @commands.command(pass_context=True)
    async def cspoll(self, ctx):
        global embed_test
        global poll_messageID
        global comp
        global custom
        global msgauthor

        comp = 0
        custom = 0
        options = 'Comp', 'Custom Game', 'No'
        reactions = ['1️⃣','2️⃣','❌']
        msgauthor = discord.Message.author
        csgo = discord.utils.get(ctx.guild.roles, id=828968453053612032)
        await ctx.message.delete()

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
        embed_test = discord.Embed(title="Counter Strike", description=''.join(description))
        await ctx.send(f'Vótáil {csgo.mention}')
        poll = await ctx.send(embed=embed_test)
        
        for reaction in reactions[:len(options)]:
            await poll.add_reaction(reaction)
        embed_test.set_footer(text='Poll ID: {}'.format(poll.id))
        print(poll.id)
        poll_messageID = poll.id



async def setup(bot):
    await bot.add_cog(VoteBot(bot))
    print('[VB] I am being loaded!')
async def teardown(bot):
    print('[VB] I am being unloaded!')