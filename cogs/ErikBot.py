import discord
import datetime
from discord import client
from discord.ext import commands, tasks
import random

client = discord.Client(intents = discord.Intents.all())

class ErikBot(commands.Cog):
    def __init__(self, bot):
        self.index = 0
        self.bot = bot
    
    global Approvals
    global Approved
    global Disaproved
    global Acknowledged
    Approvals = 0
    Approved = 0
    Disaproved = 0
    Acknowledged = 0


    @commands.command()
    ##offical old style
    async def approved(self, ctx):
        global Approvals
        Approvals = Approvals + 1
        await ctx.message.delete()
        embed = discord.Embed(title="Erik Approves", colour=discord.Colour(0x00000)) 
        embed.set_image(url="https://i.imgur.com/kmPbkWj.png")
        embed.set_footer(text='Sent By: {}. Number: {}'.format(ctx.message.author, Approvals))
        await ctx.send(embed=embed)
       ##await ctx.send('https://i.imgur.com/kmPbkWj.png')


    
    @commands.command()
    async def approve(self, ctx):
        global Approved
        Approved = Approved + 1
        await ctx.message.delete()
        embed = discord.Embed(title="Erik Approves", colour=discord.Colour(0x055c06)) 
        embed.set_image(url="https://i.imgur.com/G4dIkbA.png")
        embed.set_footer(text='Sent By: {}. Number: {}'.format(ctx.message.author, Approved))       
        await ctx.send(embed=embed)

        ##await ctx.send('https://i.imgur.com/G4dIkbA.png')
        

    @commands.command()
    async def disapprove(self, ctx):
        global Disaproved
        Disaproved = Disaproved + 1
        await ctx.message.delete()
        embed = discord.Embed(title="Erik Disapproves", colour=discord.Colour(0xcb130c)) 
        embed.set_image(url="https://i.imgur.com/Z79G2ei.png")
        embed.set_footer(text='Sent By: {}. Number: {}'.format(ctx.message.author, Disaproved))        
        await ctx.send(embed=embed)
        ##await ctx.send('https://i.imgur.com/Z79G2ei.png')
        
    
    @commands.command()
    async def acknowledge(self, ctx):
        global Acknowledged
        Acknowledged = Acknowledged + 1
        await ctx.message.delete()
        embed = discord.Embed(title="Erik Acknowledges", colour=discord.Colour(0xc6cb0c)) 
        embed.set_image(url="https://i.imgur.com/mOpx2g7.png")
        embed.set_footer(text='Sent By: {}. Number: {}'.format(ctx.message.author, Acknowledged))        
        await ctx.send(embed=embed)
        ##await ctx.send('https://i.imgur.com/mOpx2g7.png')
        
    
    @commands.command()
    async def count(self, ctx):
        global Approvals
        global Approved
        global Disapproved
        global Acknowledged
        await ctx.message.delete()
        embed = discord.Embed(title="Erik's Approvals", colour=discord.Colour(0x055c06)) 
        embed.add_field(name=f"Approved: ", value=Approvals, inline=False) 
        ##embed.set_image(url="https://i.imgur.com/kmPbkWj.png")
        embed.add_field(name=f"Approves: ", value=Approved, inline=False)
        ##embed.set_image(url="https://i.imgur.com/kmPbkWj.png")
        embed.add_field(name=f"Disapproves: ", value=Disaproved, inline=False)
        ##embed.set_image(url="https://i.imgur.com/Z79G2ei.png")
        embed.add_field(name=f"Acknowledges: ", value=Acknowledged, inline=False)
        ##embed.set_image(url="https://i.imgur.com/mOpx2g7.png")
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text='Requested By: {0}'.format(ctx.message.author))
        await ctx.send(embed=embed)

       

    @commands.command()
    async def slap(self, ctx, member : discord.Member):
        author = ctx.message.author
        ment = member.mention
        await ctx.message.delete()
        if author == member:
            await ctx.send(ctx.message.author.mention + ' Why you hitting yourself?')
        else:
            await ctx.send('Slaps {0}!'.format(ment))

    @commands.command()
    async def gerry(self, ctx, *options: str):
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
        await ctx.reply(result)


async def setup(bot):
    await bot.add_cog(ErikBot(bot))
    print('[EB] I am being loaded!')
async def teardown(bot):
    print('[EB] I am being unloaded!')

    

