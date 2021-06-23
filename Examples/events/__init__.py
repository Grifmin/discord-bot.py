'''
This cog should help deal with all events.
'''
from .command_events import CommandEvents
from .events import Events
from .process_commands import ProcessCommands


def setup(client) -> None:
    client.add_cog(CommandEvents(client))
    client.add_cog(Events(client))
    client.add_cog(ProcessCommands(client))
