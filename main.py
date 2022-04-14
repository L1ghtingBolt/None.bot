# Make a discord bot using Nextcord
from discord import Embed, Game
from nextcord.ext import commands
from os import environ as env
from fun import Fun
from help import HelpCommand
from testing import Testing
from moderation import Moderation
from asciicog import Ascii
from settings import prefix
from pyfiglet import FigletFont, figlet_format

from dotenv import load_dotenv
load_dotenv()

bot = commands.Bot(command_prefix=prefix)

bot.help_command = HelpCommand(paginator=commands.Paginator(prefix='', suffix=''))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.channel.send(embed=Embed(
            title="Error!",
            description=f"Command not found! Do {prefix}help for a list of commands.\n{error}",
            color=0xff0000
        ))
        return
    if isinstance(error, commands.MissingPermissions):
        await ctx.channel.send(embed=Embed(
            title="Error!",
            description=f"You don't have permissions to perform this action!\n{error}",
            color=0xff0000
        ))
        return
    if isinstance(error, commands.MemberNotFound):
        await ctx.channel.send(embed=Embed(
            title="Error!",
            description="Member not found! Is it a bot?",
            color=0xff0000
        ))
        return
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.channel.send(embed=Embed(
            title="Error!",
            description=f"Missing argument(s)!\n{error}",
            color=0xff0000
        ))
        return
    if isinstance(error, commands.BadArgument):
        await ctx.channel.send(embed=Embed(
            title="Error!",
            description=f"Bad argument(s)!\n{error}",
            color=0xff0000
        ))
        return
    try:
        await ctx.channel.send(embed=Embed(
                title="Error!",
                description=f"Unknown error!\n**Message:** {error}",
                color=0xff0000
            ))
    except:
        raise error

@bot.event
async def on_ready():
    print("Bot is now loaded as {}".format(bot.user.name))
    await bot.change_presence(activity=Game(name=f"{prefix}help"))

# Now we add cogs (categories)
bot.add_cog(Testing(bot))
bot.add_cog(Moderation(bot))
bot.add_cog(Ascii(bot))
bot.add_cog(Fun(bot))

bot.run(env['TOKEN'])