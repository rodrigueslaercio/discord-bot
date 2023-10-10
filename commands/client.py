import discord, sys, os

from discord.flags import Intents
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from classes.ping_pong import PingPong

class BotClient(discord.Client):

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        # replies pong! when called 
        if message.content.startswith('!ping'):
            pong = PingPong()
            await message.reply(pong.pong(), mention_author=True)

        # TODO
        if message.content.startswith('!embed'):
            embed = discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=0xFF5733)
            await message.reply(embed=embed)


