'''
This will help load in each cog
'''
from datetime import datetime
from .events import *  # must import '.filename'
from .Loader import * 
from .main import * 
from .moderation import * 

def load(client):
    '''Will help setup cogs'''
    client.launch_time = datetime.utcnow()

    client.load_extension(Loader.__name__)
    client.load_extension(main.__name__)
    client.load_extension(moderation.__name__)
    client.load_extension(events.__name__)
    # To load your own extension, uncomment the following try block. Then put in your filename (without a '.' this time).
    # try:
    #     client.load_extension(REPLACE ME.__name__)
    # except Exception as e:
    #     print(f'Error {e}')
