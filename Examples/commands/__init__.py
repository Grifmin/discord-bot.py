from .main import StandardCommands
from .moderation import Moderation


def setup(client) -> None:
    """
    This sets up commands for the basic commands
    """
    client.add_cog(StandardCommands(client))
    client.add_cog(Moderation(client))
