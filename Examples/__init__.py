'''
This will help load in each cog
'''
from datetime import datetime
from . import events   # must import '.filename'
from . import owner
from . import commands


def load(client):
    '''Will help setup cogs'''
    client.strip_after_prefix = True  # just a nice little touch.

    # sets the clients uptime for other commands to beable to access.
    client.launch_time = datetime.utcnow()

    @client.event
    async def on_message(message) -> None:
        '''
        This funtion overrides the bot events,
        preventing the bot from processing commmands.
        '''
        return

    client.load_extension(owner.__name__)
    client.load_extension(events.__name__)
    client.load_extension(commands.__name__)

    # To load your own extension, uncomment the following try block.
    # Then put in your filename (without a '.' this time).
    # try:
    #     client.load_extension(REPLACE ME.__name__)
    # except Exception as e:
    #     print(f'Error {e}')
