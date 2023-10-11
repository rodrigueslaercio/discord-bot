from dotenv import load_dotenv
from config.client import Client
import os

# loads and gets the env var
load_dotenv()
TOKEN = os.getenv('TOKEN')

# starts the bot
client = Client()
client.run(TOKEN)