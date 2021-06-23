import discord
from discord.ext import commands
from discord.ext.commands import Greedy


class Moderation(commands.Cog):
    """
    These commands are for moderating discord channels.
    """

    def __init__(self, client):
        self.client = client
        self.purge_delay = 15

    @commands.command(name='slowmode', aliases=['slowmo', 'sm'])  # command aliases can be in a list
    @commands.has_permissions(manage_messages=True, manage_channels=True)
    # ^ if you have either of these permissions you can manually set the delay without the bot.
    @commands.bot_has_permissions(manage_messages=True, manage_channels=True)
    # ^ this checks to see if the bot can manage the permissions as well
    async def _channel_slow_mode(self, ctx, delay: int = 0):
        """
        Sets the slowmode of the current chat to 'delay'
        Only works if you have `manage_messages` or `manage_channel`
        """
        await ctx.channel.edit(slowmode_delay=delay)

    @commands.command(name='clear', aliases=['purge'])
    @commands.bot_has_permissions(manage_messages=True, read_message_history=True)
    @commands.has_permissions(manage_messages=True)
    async def _purge(self, ctx, users: Greedy[discord.Member], number: int = 5):
        """
        This command will clear(or purge) a selected amount of messages.
        A user can be specified for messages to be removed.
        """

        class Purge(object):  # example of a command utilizing a subclass
            """
            Needed to setup a subclass to manage itself
            Couldn't figure out another way to do this,
            So instead i just setup this temporary class
            """
            def __init__(self, context, members, num):
                self.ctx = context
                self.users = members
                self.number = num

            def lower(self) -> None:
                self.number -= 1

            def purge_check(self, message):
                if message == self.ctx.message:
                    return True  # delete the command issuing message
                elif self.number > 0:
                    if len(self.users) == 0 or message.author in self.users:
                        self.lower()
                        return True
                return False

            async def purge(self, delay):
                total = await self.ctx.channel.purge(limit=max(self.number ** 2, 100), check=self.purge_check)
                await self.ctx.send(f"Purged {len(total) - 1} messages", delete_after=delay)

        tmp = Purge(ctx, users, number)
        await tmp.purge(self.purge_delay)


def setup(client):
    client.add_cog(Moderation(client))
