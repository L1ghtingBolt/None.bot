import nextcord
from nextcord.ext import commands
import discord
import itertools

class HelpCommand(commands.DefaultHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            emby = discord.Embed(title="None.bot Help", description=page, color=0xff0000)
            await destination.send(embed=emby)

    def get_ending_note(self):
        command_name = self.invoked_with
        return (
            f"\nType `{self.context.clean_prefix}{command_name}` `<command>` for more info on a command.\n"
            f"You can also type `{self.context.clean_prefix}{command_name}` `<category>` for more info on a category."
        )

    async def send_bot_help(self, mapping):
        ctx = self.context
        bot = ctx.bot

        if bot.description:
            # <description> portion
            self.paginator.add_line(bot.description, empty=True)

        no_category = f'\u200b\n__***Misc***__:'

        def get_category(command, *, no_category=no_category):
            cog = command.cog
            return "\n__***{}***__".format(cog.qualified_name) + ':' if cog is not None else no_category

        filtered = await self.filter_commands(bot.commands, sort=True, key=get_category)
        max_size = self.get_max_size(filtered)
        to_iterate = itertools.groupby(filtered, key=get_category)

        # Now we can add the commands to the page.
        for category, commands in to_iterate:
            commands = sorted(commands, key=lambda c: c.name) if self.sort_commands else list(commands)
            self.add_indented_commands(commands, heading=category, max_size=max_size)

        note = self.get_ending_note()
        if note:
            self.paginator.add_line()
            self.paginator.add_line(note)

        await self.send_pages()
    def add_indented_commands(self, commands, *, heading, max_size=None):
        if not commands:
            return

        self.paginator.add_line(heading)
        max_size = max_size or self.get_max_size(commands)

        get_width = nextcord.utils._string_width
        for command in commands:
            name = '*`{}`*'.format(command.name)
            width = max_size - (get_width(name) - len(name))
            entry = f'{self.indent * " "}{name:<{width}} {command.short_doc}'
            self.paginator.add_line(self.shorten_text(entry))
