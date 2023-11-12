from discord.ext import commands
import discord

class Client(commands.Bot):
    """class for the bot client"""
    def __init__(self):
        super().__init__(
            command_prefix = commands.when_mentioned_or("&"),
            intents = discord.Intents.all(),
            help_command = commands.DefaultHelpCommand(dm_help=True)
        )

    async def on_member_join(self, member):
        """sends a welcoming message on member join"""
        guild = member.guild
        if guild.system_channel is not None:
            await guild.system_channel.send(f"Bem-vindo {member.mention} ao {guild.name}")
         
    async def setup_hook(self):
        """overwrites the handler loading the cogs"""
        await self.load_extension('cogs.ping_pong_cmd')
        await self.load_extension('cogs.user_cmd')
        await self.tree.sync()
        print("Cogs loaded successfully")


