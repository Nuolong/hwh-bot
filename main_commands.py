from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="`")

@commands.command()
async def ping(ctx):
	await ctx.send("Test")

bot.add_command(ping)

@commands.command(description="Provide args", brief="Brief msg in `help")
async def hello(ctx, *args):
	if len(args) > 0:
		await ctx.send(" ".join(args))
	else:
		return

bot.add_command(hello)

bot.run(TOKEN)
