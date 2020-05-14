# bot.py

import os
import random

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

@client.event
async def on_member_join(member):
	await member.create_dm()
	await member.dm_channel.send(f'Heblo {member.name}, welcome to this bot test!!!111')	

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    test_responses = ['test a','test b','test c']

    if message.content == 'test!':
        response = random.choice(test_responses)
        await message.channel.send(response)


@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


client.run(TOKEN)
