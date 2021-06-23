import os, discord
from discord.ext import commands


def prefix(client, message):
    '''
    Function will return prefixs to bot.
    On every message it will check if the message is sent starting with the prefix
    hence, this function needs the parameters client and message.
    client = bot, sometimes I use them interchangeably. Sorry in advanced
    '''
    return_prefix = '-'
    return commands.when_mentioned_or(return_prefix)(client, message)

TOKEN = ''  # define as blank for now.

INTENTS = discord.Intents.all()

try:  # this block of try statements is to attempt and obtain a token.
    TOKEN = os.getenv['TOKEN']
except Exception as e:
    try:
        path = os.path.dirname(__file__)
        TOKEN = open(path + '/login', 'r').read()
    except Exception as e:
        pass  # could not find any token
