import os

from discord.ext import commands

from settings import *

# bot command prefix
bot = commands.Bot(command_prefix="`")

# automatically loads the cog files in cogs directory
for filename in os.listdir("./cogs"):
	if filename.endswith(".py") and filename != "__init__.py":
		bot.load_extension(f'cogs.{filename[:-3]}')


bot.run(DISCORD_BOT_TOKEN)
