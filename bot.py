from discord.ext import commands


def get_prefix(client, message):
    """
    On every message it will check if the message is sent starting with the prefix
    hence, this function needs the parameters client and message.
    client = bot, sometimes I use them interchangeably. Sorry in advanced
    """
    prefix = '-'  # can be whatever prefix or call another function
    return prefix


bot = commands.Bot(command_prefix=get_prefix)


def initialize():
    """
    This function will try to initiate any Cogs if it can, otherwise will output an error
    """
    # done; finished. Todo; main, events
    extensions = [
        'Examples.Loader',  # To load extensions, you must do FolderName.FileName without .py
        'Examples.main',
        'Examples.events'
    ]
    for extension in extensions:
        try:
            bot.load_extension(extension)
            print(f'Loaded {extension}')  # console output is nice sometimes
        except Exception as e:
            print(f'Failed to load {extension}. Error {e}')


initialize()  # will load extension cogs before attempting to login to discord
#bot.run('a_really_neat_token')  # example login, not recomended
bot.run(open('login', 'r').read())  # much better login
