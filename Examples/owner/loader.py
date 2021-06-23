from discord.ext import commands


def is_owner():
    """
    A neat example of setting up custom checks for the Examples.
    """

    def predicate(ctx):
        """
        This will get the ctx from the command check. (ie: you can use all ctx.message, author, etc methods)
        """
        owner_id = [12345]  # could have multiple users use this.
        owner_id.append(ctx.bot.owner_id)  # makes sure the bots owner id is in the list.
        return ctx.author.id in owner_id

    return commands.check(predicate)


class Loader(commands.Cog, command_attrs=dict(hidden=True)):
    """
    This class is designed for reloading, loading, and unloading of cogs
    Will reload, load, unload cog's while the bot is running. Useful rapid debugging and testing
    The 'command_attrs=dict(hidden=True)' parameter just sets these Examples to be hidden by default
    Instead of using 'hidden=True' for each command you want hidden
    """

    def __init__(self, client):
        self.client = client

    @commands.command(name='load')  # sets up command, can define name
    @commands.is_owner()  # only the bot owner can run these.
    async def _load(self, ctx, cog: str = None):
        """
        Will attempt to load cog if it can
        """
        if cog is not None:
            try:
                self.client.load_extension(cog)
                await ctx.send(f'Loaded {cog}')
            except Exception as e:
                await ctx.send(f'Error while loading {cog}. `{e}`')
                pass

    @commands.command(name='reload')
    @commands.check(is_owner())  # in case you want to set up your own check
    async def _reload(self, ctx, cog: str = None):
        """
        Will attempt to reload cog if specified.
        Otherwise will reload all currently loaded cogs if it can.
        """
        if cog in ['*', '', None]:
            extensions_dat = self.client.extensions
            extensions = list(extensions_dat.keys())
            total, reloaded = len(extensions), 0
            for extension in extensions:
                try:
                    self.client.reload_extension(extension)
                    reloaded += 1
                except Exception as e:
                    await ctx.send(f'Error while reloading {extension}. `{e}`')
            await ctx.send(f'Reloaded {reloaded} of {total} Cogs')
        else:
            try:
                self.client.reload_extension(cog)
                await ctx.send(f'Reloaded {cog}')
            except Exception as e:
                await ctx.send(f'Error could not reload {cog}; `{e}`')

    @commands.command(name='unload')
    @commands.is_owner()  # much easier check.
    async def _unload(self, ctx, cog: str = None):
        """
        Will attempt to unload specific cog.
        """
        loaded_cogs = self.client.extensions
        if cog in loaded_cogs:
            try:
                self.client.unload_extension(cog)  # ideally, you setup all your cogs to lowercase
            except Exception as e:
                await ctx.send(f"Failed to unload cog: `{cog}`, Error: `{e}`")

    @commands.command(name='cogs', aliases=['extensions'])
    @commands.is_owner()
    async def _cogs(self, ctx):
        """
        Will send the user a list of currently loaded cogs.
        """
        cogs = self.client.extensions
        cog_keys = list(cogs)
        message = "**Cogs**: "
        for cog_name in cog_keys:
            message += f"`{cog_name}` "
        await ctx.send(message)


def setup(client):
    """
    All cogs must have this setup function.
    """
    client.add_cog(Loader(client))
