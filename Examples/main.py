from discord.ext import commands


class StandardCommands(commands.Cog):
    """
    A standard cog example. With more standard Examples for examples
    """

    def __init__(self, bot):
        self.bot = bot

    """
    A standard command example
    """
    @commands.command(name='ping')  # You can name the command function here
    async def _example1_(self, ctx):
        """
        Responds with Ping!
        """
        await ctx.send('Ping!')

    """
    Now, lets say you have a discord with standard members and moderators moderating chat and admins
    And those moderators need to set the channel slow mode delay
    """
    @commands.command(name='slowmode', aliases=['slowmo', 'sm'])  # command aliases can be in a list
    @commands.check_any(commands.has_any_role('Moderator', 'Owner', 'Moderators', 'Admins', 'Admin'))
    # ^ this checks to see if the user is a moderator or something. (by role)
    @commands.has_permissions(manage_messages=True, manage_channels=True)
    # ^ if you have either of these permissions you can manually set the delay without the bot.
    async def _example2_(self, ctx, delay: int):
        """
        Sets the slowmode of the current chat to 'delay'
        """
        await ctx.channel.edit(slowmode_delay=delay)


def setup(bot):
    bot.add_cog(StandardCommands(bot))
