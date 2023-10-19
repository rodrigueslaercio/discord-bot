from discord.ext import commands
import discord

class Client(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix = commands.when_mentioned_or("&"),
            intents = discord.Intents.all(),
            help_command = commands.DefaultHelpCommand(dm_help=True)
        )

    # sends a welcoming message on member join
    async def on_member_join(self, member):
           guild = member.guild
           if guild.system_channel is not None:
                  await guild.system_channel.send(f"Bem-vindo {member.mention} ao {guild.name}")
         
    # overwriting the handler loading the cogs
    async def setup_hook(self):
                await self.load_extension('cogs.ping_pong_cmd')
                await self.load_extension('cogs.user_cmd')
                await self.tree.sync()
                print("Cogs loaded successfully")


