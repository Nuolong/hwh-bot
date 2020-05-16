import aiohttp
from discord.ext import commands
import discord

class Images(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def cat(self, ctx):
		async with ctx.channel.tpying():
			async with aiohttp.ClientSession() as cs:
				async with cs.get("http://aws.random.cat/meow") as r:
					data = await r.json()
				
					embed = discord.Embed(title="Cat")
					embed.set_image(url=data['file'])
					embed.set_footer(text="http://random.cat/")

					await ctx.send(embed=embed)
		
