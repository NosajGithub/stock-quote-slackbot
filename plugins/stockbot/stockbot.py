import random
import time
import re
import yaml

from slackclient import SlackClient
from yahoo_finance import Share

crontable = []
outputs = []

config = yaml.load(file('rtmbot.conf', 'r'))
trig_word = config["TRIGGER_WORD"]

def process_message(data):
    
    message=data["text"]
    muser=data["user"]
    uid=str(muser)
    
    if trig_word in message:
        print message
        rest_of_message = re.sub(trig_word, '', message.lower())
        tline=rest_of_message.split()
        if len(tline) >= 10:
            outputs.append([data['channel'], "Too many stocks to look up! Try again with fewer than 10"])
        else:
            for word in tline:
                cleanword=re.sub('[@<>]', '', word)
                quote = Share(cleanword).get_price()
                if quote != None:
                    outputs.append([data['channel'], "The current stock price for \'" + cleanword.upper() +
                                      "\' is: $" + str(quote)])
                else:
                    outputs.append([data['channel'], "Can't find a stock with the symbol \'" + cleanword.upper() + "\'"])