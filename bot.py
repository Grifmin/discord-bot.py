from discord.ext import commands


def get_prefix(client, message):
    """
    On every message it will check if the message is sent starting with the prefix
    hence, this function needs the parameters client and message.
    client = bot, sometimes I use them interchangeably. Sorry in advanced
    """
    prefix = '-'  # can be whatever prefix or call another function
    return commands.when_mentioned_or(prefix)(client, message)


client = commands.Bot(command_prefix=get_prefix)


def initialize():
    """
    This function will try to initiate any Cogs if it can, otherwise will output an error
    """
    extensions = open('config/cogs', 'r').readlines()  # allows bot to read extensions from file.
    for extension in extensions:
        extension = extension.replace('\n', '')
        try:
            client.load_extension(extension)
            print(f'Loaded {extension}')  # console output is nice sometimes
        except Exception as e:
            print(f'Failed to load {extension}. Error {e}')


initialize()  # will load extension cogs
#bot.run('a_really_neat_token')  # example login, not recommended
client.run(open('config/login', 'r').read(), reconnect=True)  # much better login
