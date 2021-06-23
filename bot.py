from discord.ext import commands
import config
import Examples


def main():
    '''Main function'''
    client = commands.Bot(command_prefix=config.prefix, intents=config.INTENTS)
    Examples.load(client)  # loads cogs and other events
    client.run(config.TOKEN, reconnect=True)  # start bot

if __name__ == '__main__':
    '''Starts the bot'''
    main()
