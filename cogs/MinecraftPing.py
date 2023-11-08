import discord
from discord.ext import commands, tasks
from discord.gateway import WebSocketClosure
from discord.utils import get
from mcstatus import JavaServer
from asyncio import sleep

mcserverip = 'mc.finneganphoto.ie'

class MinecraftPing(commands.Cog):
    def __init__(self, bot):
        self.index = 0
        self.bot = bot
        self.ping.start()

    def cog_unload(self):
        self.ping.cancel()

    @tasks.loop(seconds=120.0)
    async def ping(self):
       # response = requests.get('https://api.mcsrvstat.us/2/mc.potat0s.com')
       # response.json
       # print(response.text)
        try:
            server = JavaServer.lookup(mcserverip)
            status = server.status()
            print("refreshing")
            await self.bot.change_presence(activity=discord.Game(name="Minecraft with {0} players.".format(status.players.online)))
            if status.players.online == 1:
                await self.bot.change_presence(activity=discord.Game(name="Minecraft with {0}.".format(str(status.players.names))))
            if status.players.online == 0:
                await self.bot.change_presence(activity=discord.Game(name="?server to request start."))
            print('server offline')
            Status = 0
            print (Status)
            await sleep(100)
        except (ConnectionError, TimeoutError, WebSocketClosure, Exception) as e:
            await self.bot.change_presence(activity=discord.Game(name=mcserverip))
            print("Server Online")
            guild1 = self.bot.get_guild(398575354090094592)
            if discord.utils.get(guild1.text_channels, name='minecraft-server'):
                channel = get(guild1.text_channels, name='minecraft-server')
                await channel.delete()
            Status = 1
            print(e)
            print (Status)
            await sleep(50)
            
    


    @ping.before_loop
    async def before_ping(self):
        print('waiting...')
        await self.bot.wait_until_ready()

async def setup(bot):
    await bot.add_cog(MinecraftPing(bot))
    print('[MP] I am being loaded!')
async def teardown(bot):
    print('[MP] I am being unloaded!')