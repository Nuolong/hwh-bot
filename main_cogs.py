import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="`")

bot.load_extension(f'cogs.test')
bot.load_extension(f'cogs.basic')

bot.run(TOKEN)
