import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6530832990:AAE-bsPEa-GT75EqAOWQ8JKfij5JjukFGEA")
    API_ID = int(os.environ.get("API_ID", 977080))
    API_HASH = os.environ.get("API_HASH", "0c20c4265501492a1513f91755acd42b")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
