from discord.ext import commands
from classes.ping_pong import PingPong

class PingPongCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.hybrid_command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def ping(self, ctx):
        pong = PingPong()
        await ctx.reply(pong.pong())

async def setup(client):
    await client.add_cog(PingPongCommand(client))