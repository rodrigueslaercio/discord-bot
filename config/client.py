from discord.ext import commands
import discord
import os
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class Client(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix = commands.when_mentioned_or("&"),
            intents = discord.Intents.all(),
            help_command = commands.DefaultHelpCommand(dm_help=True)
        )
    
    async def setup_hook(self): #overwriting a handler
                await self.load_extension('cogs.cogs_slash_test')
                await self.load_extension('cogs.ping_pong_cmd')
                await self.tree.sync()
                print("Cogs loaded successfully")


