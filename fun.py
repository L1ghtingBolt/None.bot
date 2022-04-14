import random
from nextcord.ext import commands
from discord import Embed
from settings import version, motivations

class Fun(commands.Cog):
    @commands.command(
        brief="Sends a poll",
        description="Sends a poll. You can specify the question and the options.\n**Example:** `n.poll Test|✅: yes,❌:no`",
    )
    async def poll(self, ctx, *, question):
        # Poll command with options
        description = question.split("|")
        options = description[1].split(",")
        optionstext = "\n".join(options)
        
        embed = Embed(
            title=f"Poll: {description[0]}",
            description=f"**Options**:\n{optionstext}",
            color=0x00ff00,
        )
        msg = await ctx.channel.send(embed=embed)
        # Add reactions
        for option in options:
            await msg.add_reaction(option[0])

    @commands.command(
        brief="Sends a random number between `<min>` and <max>",
        description="Sends a random number between `<min>` and `<max>`",
    )
    async def random(self, ctx, min=0, max=100):
        await ctx.send(embed=Embed(
            title="Random number",
            description=random.randint(int(min),int(max)),
            color=0x00ff00
        ))

    @commands.command(
        brief="Sends the message you tell the bot.",
        description="Sends the message you tell the bot.",
    )
    async def say(self, ctx, *, text):
        await ctx.send(embed=Embed(
            title="Saying...",
            description=text,
            color=0x00ff00
        ))

    @commands.command(
        brief="Tells you the bot version.",
        description="Tells you the bot version.",
    )
    async def version(self, ctx):
        await ctx.send(embed=Embed(
            title="Version:",
            description=version,
            color=0x00ff00
        ))

    @commands.command(
        brief="Tells you a motivational phrase.",
        description="Tells you a motivational phrase.",
    )
    async def motivation(self, ctx):
        await ctx.send(embed=Embed(
            title="Motivation",
            description=motivations[random.randint(0,len(motivations)-1)],
            color=0x00ff00
        ))