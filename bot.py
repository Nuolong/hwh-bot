# bot.py

import os
import random
from dotenv import load_dotenv

import discord
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='`')

@bot.event
async def on_ready():
    print(f'{bot.user.name} connected to Discord.\n')


@bot.command(name='test', help='Just a test command.')
async def test(ctx):
	test_pile = ['heblo','byeblo','test3']
	response = random.choice(test_pile)
	await ctx.send(response)

@bot.command(name='roll', help='Simulates rolling dice. `roll [dice] [sides]')
async def roll(ctx, number_of_dice: int=1, number_of_sides: int=6):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name='mkch')
@commands.has_role('TestRole')
async def create_channel(ctx, channel_name='test-channel'):
	guild = ctx.guild

	#checks for if the channel doesn't already exist
	if not discord.utils.get(guild.channels, name=channel_name):
		print(f'Creating a new channel: {channel_name}')
		await guild.create_text_channel(channel_name)
		await ctx.send(f'Created channel: {channel_name}')
	else:
		await ctx.send('Cannot create channel. Channel already exists.')

# broken for now
@bot.command(name='rmch')
@commands.has_role('TestRole')
async def remove_channel(ctx, channel_name='test-channel'):
    guildC = ctx.GuildChannel

    #checks for if the channel already exists
    if discord.utils.get(guildC, name=channel_name):
        print(f'Removing the channel: {channel_name}')
        await guildC.delete(channel_name)
        await ctx.send(f'Removed channel: {channel_name}')
    else:
        await ctx.send('Cannot remove channel. Channel does not exist.')

bot.run(TOKEN)

