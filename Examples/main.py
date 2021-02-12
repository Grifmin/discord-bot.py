from discord.ext import commands


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


def setup(client):
    client.add_cog(StandardCommands(client))
