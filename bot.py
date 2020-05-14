# bot.py

import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
	guild = discord.utils.get(client.guilds, name=GUILD)	

	print(f'{client.user} is connected to:\n'
		f'{guild.name}(id: {guild.id})\n')

	members = '\n - '.join([member.name for member in guild.members])
	print(f'Server Members:\n - {members}')
	



client.run(TOKEN)
