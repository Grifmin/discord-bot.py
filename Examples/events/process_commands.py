from discord.ext import commands


class ProcessCommands(commands.Cog, name='Process commands'):
    '''
    This class manages the processing of commands
    It is important to have this cog loaded if you plan on using commands
    Without this cog loaded, all messages will be ignored
    Only events can be seen from the bot if you do not process the message
    '''
    def __init__(self, client) -> None:
        super().__init__()
        self.client = client

    @commands.Cog.listener(name='on_message')
    async def on_message(self, message):
        """
        Earlier, in 'Examples/__init__.py' we did:
            @client.event
            async def on_message(message):
                return
        This stops discord api from processing commands,
        However, we can still listen to events.
        Now we can control the processing of commands from here.
            (will be used in a later example)
        """
        await self.client.process_commands(message)


def setup(client) -> None:
    '''
    This sets up the bot like normal so it can recieve and process commands.
    '''
    client.add_cog(ProcessCommands(client))
