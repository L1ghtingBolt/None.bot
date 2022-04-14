from nextcord.ext import commands
from discord import Embed
import discord

class Moderation(commands.Cog):
    @commands.command(
        brief="Kicks a user from the server.",
        description="Kicks a user from the server. You can specify the reason.",
    )
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="Not a good boy!"):
        if member == ctx.author:
            await ctx.channel.send(embed=Embed(
                title="Error!",
                description="You can't kick yourself!",
                color=0xff0000
            ))
            return
        if member.guild_permissions.administrator:
            await ctx.channel.send(embed=Embed(
                title="Error!",
                description="You can't kick an administrator!",
                color=0xff0000
            ))
            return
        if member.guild_permissions.kick_members:
            await ctx.channel.send(embed=Embed(
                title="Error!",
                description="You can't kick a moderator!",
                color=0xff0000
            ))
            return
        await member.kick(reason=reason)
        await ctx.channel.send(embed=Embed(
            title="Success!",
            description="{} has been kicked from the server!\nReason: {}".format(member.mention, reason),
            color=0x00ff00
        ))
    @commands.command(
        brief="Bans a user from the server.",
        description="Bans a user from the server. You can specify the reason.",
    )
    @commands.has_permissions(kick_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="Not a good boy!"):
        if member == ctx.author:
            await ctx.channel.send(embed=Embed(
                title="Error!",
                description="You can't ban yourself!",
                color=0xff0000
            ))
            return
        if member.guild_permissions.administrator:
            await ctx.channel.send(embed=Embed(
                title="Error!",
                description="You can't ban an administrator!",
                color=0xff0000
            ))
            return
        if member.guild_permissions.kick_members:
            await ctx.channel.send(embed=Embed(
                title="Error!",
                description="You can't ban a moderator!",
                color=0xff0000
            ))
            return
        await member.ban(reason=reason)
        await ctx.channel.send(embed=Embed(
            title="Success!",
            description="{} has been banned from the server!\nReason: {}".format(member.mention, reason),
            color=0x00ff00
        ))
    @commands.command(
        brief="Warns a user from the server.",
        description="Warns a user from the server. You can specify the reason.",
    )
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, member: discord.Member, *, reason="Not a good boy!"):
        await ctx.channel.send(embed=Embed(
            title=f"Warn",
            description=f"***Reason***: {reason}\n***Member***: {member.mention if not member.bot else member.nick}",
            color=0xff0000
        ))

    # Clear message
    @commands.command(
        brief="Clears a number of messages.",
        description="Clears a number of messages.",
    )
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)
        await ctx.channel.send(embed=Embed(
            title="Success!",
            description="{} messages have been deleted!".format(amount),
            color=0x00ff00
        ))