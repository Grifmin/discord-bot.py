from .loader import Loader


def setup(client) -> None:
    client.add_cog(Loader(client))
