import discord, os
from dotenv import load_dotenv
from discord.ext import commands
from classes import *
from commands.client import BotClient

# loads and gets the env var
load_dotenv()
TOKEN = os.getenv('TOKEN')

# sets the intents
intents = discord.Intents.default()
intents.message_content = True

# starts the client
client = BotClient(intents=intents)
client.run(TOKEN)
