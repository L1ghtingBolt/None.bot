from discord import Embed
from nextcord.ext import commands
from settings import prefix
from pyfiglet import Figlet, FigletFont
f = Figlet()

class Ascii(commands.Cog):
    @commands.command(
        brief="Converts text to ASCII art",
        description="Converts `<text>` to ascii art.".format(prefix),
    )
    async def ascii(self, ctx, fontname, *args):
        try:
            f.setFont(font=fontname)
            text = f.renderText(" ".join(args))

            await ctx.channel.send("```{}```".format(text))
        except:
            emb = Embed(
                title="Error!",
                color=0xff0000,
                description="Unknown font!"
            )
            await ctx.channel.send(embed=emb)

    @commands.command(
        brief="Sends a list of the default fonts.",
        description="Lists all the fonts available to use with ascii.".format(prefix)
    )
    async def fonts(self, ctx):
        await ctx.channel.send(embed=Embed(
            title="Available Fonts",
            color=0xff0000,
            description=", ".join(f.getFonts())
        ))