from discord.ext import commands
import discord


class CommandEvents(commands.Cog):
    """
    This Class is for command events.
    Will also help filter out command erros that get logged into console
    """

    def __init__(self, client) -> None:
        self.client = client
        super().__init__()

    @commands.Cog.listener(name='on_command_error')
    async def cmd_error(self, ctx, error):
        """
        Will reduce amount of console output
        """
        if isinstance(error, commands.CommandNotFound):
            return  # user said {prefix}{something} but there wasnt a command
        elif isinstance(error, commands.CommandInvokeError):
            return  # user did not execute the command correctly
        elif isinstance(error, discord.errors.Forbidden):
            return  # the bot probably doesnt have permission
        elif isinstance(error, commands.CommandOnCooldown):
            return  # command has a cooldown
        elif isinstance(error, commands.NotOwner):
            return  # not the bot owner
        else:
            print(f'Error: {error}', type(error))

    @commands.Cog.listener(name='on_command_completion')
    async def cmd_complete(self, ctx):
        """
        A command was just completed,
        could add a command counter here if wanted
        """
        pass


def setup(client) -> None:
    '''Basic setup Cog'''
    client.add_cog(CommandEvents(client))
