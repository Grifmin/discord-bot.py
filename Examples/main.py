from discord.ext import commands
from datetime import datetime


def send_msg():
    """
    Example on a check to make sure the bot itself can send messages in issued channel
    """
    def predicate(ctx):
        return ctx.channel.permissions_for(ctx.guild.me).send_messages

    return commands.check(predicate)


class StandardCommands(commands.Cog, name='Standard'):
    """
    A standard cog example. With more standard Examples for examples
    """

    def __init__(self, client):
        self.client = client

    def get_uptime(self) -> str:
        '''Returns uptime in a neatly formatted string'''
        delta_uptime = datetime.utcnow() - self.client.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        min, sec = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        weeks, days = divmod(days, 7)

        msg = ('', f'{weeks}w, ')[weeks > 0] + ('', f'{days}d, ')[days > 0] + (
            '', f'{hours}hr, ')[hours > 0] + ('', f'{min}m, ')[min > 0] + f'{sec}sec'
        return msg

    """
    A standard command example
    """

    @commands.command(name='ping')  # You can name the command function here
    @send_msg()
    async def _example1(self, ctx):
        """
        Responds with Pong!
        """
        await ctx.send('Pong!')

    @commands.command(name='latency')
    @send_msg()
    async def _example2(self, ctx):
        """
        Responds with the client's latency
        """
        latency = round(self.client.latency * 1000)
        await ctx.send(f'Clients latency `{latency}ms`')

    @commands.command(name='uptime')
    # much easier version of '@send_msg' implementation
    @commands.bot_has_permissions(send_messagse=True)
    async def _uptime(self, ctx):
        """Returns uptime"""
        await ctx.send(f'`{self.get_uptime}`')


def setup(client):
    client.add_cog(StandardCommands(client))
