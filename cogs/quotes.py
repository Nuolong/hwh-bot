import discord
from discord.ext import commands

from utils import get_quote

class Quotes(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def quote(self, ctx):
		quoteString = await get_quote()
		await ctx.send(quoteString)

def setup(bot):
	bot.add_cog(Quotes(bot))
