import discord
from discord.ext import commands


async def check_blacklist(message):
    """
    An example of a blacklisting words
    """
    message_str = message.content
    blacklist = ['yeeteth', 'blacklisted_word']  # not a great example, but you can technically do this
    # ideally, should open this list from a file
    for i in blacklist:
        if i.lower() in message_str.lower():  # want to make sure they are both lowercase
            await message.delete()  # delete the blacklisted word


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener(name='on_message')
    async def _message_send(self, message):
        """
        Event occurs when a user sends any message
        """
        await check_blacklist(message)

    @commands.Cog.listener(name='on_message_edit')
    async def _message_edit(self, before, after):
        """
        Before and after are the exact same as the message object in on_message event
        """
        await check_blacklist(after)  # check the new message (edited bit)
        # you could also implement a logger here, but im not going to show you how to do that

    @commands.Cog.listener(name='on_command_error')
    async def _on_command_error(self, ctx, error):
        """
        Will help reduce the amount of console output
        """
        if isinstance(error, commands.CommandNotFound):
            return  # the user said something that isn't a command
        elif isinstance(error, commands.CommandInvokeError):
            return  # the user did not type the subcommand correctly
        elif isinstance(error, discord.errors.Forbidden):
            # You can technically do this but i would not suggest it
            # await ctx.author.send(f"Error: {error}")  # just an example
            return  # forbidden to do this, probably unable to send message?
        else:
            print(f"Error: {error}")


def setup(bot):
    bot.add_cog(Events(bot))
