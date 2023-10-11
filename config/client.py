from discord.ext import commands
import discord
import os

class Client(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix = commands.when_mentioned_or("&"),
            intents = discord.Intents.all(),
            help_command = commands.DefaultHelpCommand(dm_help=True)
        )
    
    # overwriting the handler loading the cogs
    async def setup_hook(self):
                await self.load_extension('cogs.ping_pong_cmd')
                await self.load_extension('cogs.user_avatar_cmd')
                await self.tree.sync()
                print("Cogs loaded successfully")


