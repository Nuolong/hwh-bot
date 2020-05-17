from discord.ext import commands
from utils import text_to_owo, text_with_baby

class Basic(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	# called when a command_error is invoked
	@commands.Cog.listener()
	async def on_command_error(self, ctx, er):
		print(er)
		await ctx.send("Basic error message for incorrect command usage")

	@commands.command()
	async def baby(self, ctx):
		await ctx.send(text_with_baby(ctx.message.content))

	# converts text to owo when `owo is written
	@commands.command()
	async def owo(self, ctx):
		await ctx.send(text_to_owo(ctx.message.content))

	# creates an invite link to the server. (only works in guild)
	@commands.command()
	@commands.guild_only()
	async def invite(self, ctx):
		link = await ctx.channel.create_invite(max_age=1) # max_age in days
		await ctx.send(link)

def setup(bot):
	bot.add_cog(Basic(bot))
