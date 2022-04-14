from nextcord.ext import commands
from discord import Embed

class Testing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        brief="Sends 'pong'. Used for testing.",
        description="Sends 'pong'. Used for testing.",
    )
    async def ping(self, ctx):
        embed = Embed(
            title='Pong!',
            description='Bot is active!',
            color=0x00ff00,
        )
        await ctx.channel.send(embed=embed)

    @commands.command(
        brief="Tells you some things about bot status.",
        description="Tell you some things about bot status. For example, how many servers the bot is in.",
    )
    async def status(self, ctx):
        servers = len(self.bot.guilds)
        embed = Embed(
            title='Status:',
            description='Bot is active on {} '.format(servers) + ("servers!" if servers != 1 else "server!"), #Yayayayayayayayay
            color=0x00ff00,
        )
        await ctx.channel.send(embed=embed)
