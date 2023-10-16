import discord
from discord import member
from discord import Client
from discord import Guild
from discord.channel import DMChannel
from discord.ext import commands, tasks
from discord.utils import get
import mcstatus
from mcstatus import JavaServer
from discord.gateway import WebSocketClosure

mcserverip = 'rytekin.aternos.me'

class MinecraftWho(commands.Cog):
    def __init__(self, bot):
        self.index = 0
        self.bot = bot

    global Requested

    @commands.command()
    async def minecraft(self, ctx):
        try:
            server = JavaServer.lookup(mcserverip)
            query = server.query()
            status = server.status()
            description = str(status.players.online)
            ping = str(status.latency) + "ms"
            players = str(query.players.names)
            print("The server has the following players online: {0}".format(", ".join(query.players.names)))

            embed = discord.Embed(title="Minebot", colour=discord.Colour(0x3e038c))

            embed.add_field(name=f"Players Online: ", value=players, inline=False)
            embed.add_field(name=f"Responded In: ", value=ping, inline=False)    
            embed.set_thumbnail(url="https://i.imgur.com/z9llKEK.jpg")

            await ctx.send(embed=embed)
        except (ConnectionError, TimeoutError, WebSocketClosure, Exception) as e:
            await ctx.send("Server is offline.")

##    @commands.command()
##    async def map(self, ctx):
##        try:
#            server = JavaServer.lookup('64.40.9.245:25565')
#            query = server.query()
#            status = server.status()
#            description = str(status.players.online)
#            ping = str(status.latency) + "ms"
#            players = str(query.players.names)
#            await ctx.send("Online map available at: http://mc.potat0s.com:4003/")
#        except (ConnectionError, TimeoutError, WebSocketClosure, Exception) as e:
#            await ctx.send("Server is offline.")

    @commands.command()
    @commands.cooldown(1, 240, commands.BucketType.user)
    async def server(self, ctx):
        global Requested
        try:
            server = JavaServer(mcserverip)
            status = server.status()
            print(ctx.message.author, ' requested')
            await ctx.message.delete()
            await ctx.send("Server start requested by {0}".format(ctx.message.author.name), delete_after=60.0)
#           nathan = await ctx.guild.fetch_member(207546950621331460)
#           denis = await ctx.guild.fetch_member(294769489118101514)
#           jaydon = await ctx.guild.fetch_member(398574966024699908)
            guild = ctx.guild
            member = ctx.author
            admin_role = get(guild.roles, name="aternos")
            overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            guild.me: discord.PermissionOverwrite(read_messages=True),
            admin_role: discord.PermissionOverwrite(read_messages=True)
            }
            channel = await guild.create_text_channel('minecraft-server', overwrites=overwrites)
            allowed_mentions = discord.AllowedMentions(everyone = True)
            await channel.send(f"@everyone {ctx.message.author.name} requesting server start", allowed_mentions = allowed_mentions)
    #        await discord.Member.send(nathan, "Server start requested by {0}".format(ctx.message.author.name))       
    #        await discord.Member.send(denis, "Server start requested by {0}".format(ctx.message.author.name))       
    #        await discord.Member.send(jaydon, "Server start requested by {0}".format(ctx.message.author.name))
            await ctx.author.send('Start request sent')
            print('Requests sent')
        except (ConnectionError, TimeoutError, WebSocketClosure, Exception) as e:
            await ctx.message.delete()   
            await ctx.author.send('Server is already online, mc.potat0s.com')       
    
async def setup(bot):
    await bot.add_cog(MinecraftWho(bot))
    print('[MW] I am being loaded!')
async def teardown(bot):
    print('[MW] I am being unloaded!')