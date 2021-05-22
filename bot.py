from discord.ext import commands
import config
import Examples


def main():
    '''Main'''
    client = commands.Bot(command_prefix=config.prefix, strip_after_prefix=True)
    Examples.load(client)
    client.run(config.TOKEN, reconnect=True)

if __name__ == '__main__':
    '''Starts the bot'''
    main()