# bot.py

import os
import random
from dotenv import load_dotenv

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


bot.run(TOKEN)

