import aiohttp
from discord.ext import commands
import discord

import random

import praw

from settings import REDDIT_APP_ID, REDDIT_APP_SECRET, REDDIT_ENABLED_SUBREDDITS

class Images(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.reddit = None
		if REDDIT_APP_ID and REDDIT_APP_SECRET:
			self.reddit = praw.Reddit(client_id=REDDIT_APP_ID,
			client_secret=REDDIT_APP_SECRET, user_agent="HWHELPER:%s:1.0" % 
			REDDIT_APP_ID)
	
	@commands.command()
	async def reddit(self, ctx, subreddit: str="aww"):
		async with ctx.channel.typing():
			if self.reddit:
				if subreddit:
					chosen_subreddit = subreddit	
				submissions = self.reddit.subreddit(chosen_subreddit).hot()
			
				picked_post = random.randint(1,5)
				for _ in range(0, picked_post):
					submission = next(x for x in submissions if not x.stickied)
				await ctx.send(submission.url)
			else:
				await ctx.send("Something is broken.")
	

	# sends a random image of a cat from http://random.cat/
	@commands.command()
	async def cat(self, ctx):
		async with ctx.channel.typing(): # feedback from the bot that it's working
			async with aiohttp.ClientSession() as cs:
				async with cs.get("http://aws.random.cat/meow") as r:
					data = await r.json()
				
					embed = discord.Embed(title="Cat")
					embed.set_image(url=data["file"])
					embed.set_footer(text="from http://random.cat/")

					await ctx.send(embed=embed)

	# sends a random dog from https://random.dog/
	@commands.command()
	async def dog(self, ctx):
		async with ctx.channel.typing():
			async with aiohttp.ClientSession() as cs:
				async with cs.get("https://random.dog/woof.json") as r:
					data = await r.json()
					
					embed = discord.Embed(title="Dog")
					embed.set_image(url=data["url"])
					embed.set_footer(text="from https://random.dog/")

					await ctx.send(embed=embed)

	

def setup(bot):
	bot.add_cog(Images(bot))		
