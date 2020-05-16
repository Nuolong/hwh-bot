import random

from discord.ext import commands

class Test(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(brief="Random number between 1 and 6")
	async def roll(self, ctx, *args):
		n = random.randrange(1, 7)
		await ctx.send(n)



def setup(bot):
	bot.add_cog(Test(bot))
