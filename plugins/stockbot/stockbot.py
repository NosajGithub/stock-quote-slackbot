import random
import time
import re
import yaml
import datetime as dt
from slackclient import SlackClient
from yahoo_finance import Share

crontable = []
outputs = []

config = yaml.load(file('rtmbot.conf', 'r'))
trig_word = config["TRIGGER_WORD"]

def process_message(data):
    """Process a message entered by a user
    If the message has the trigger word, evaluate it and respond

    data -- the message's data
    """
    message = data["text"]
    
    # Look for trigger word, remove it, and look up each word
    if trig_word in message:
        print message
        rest_of_message = re.sub(trig_word, '', message.lower())
        tline=rest_of_message.split()
        if len(tline) >= 10:
            outputs.append([data['channel'], "Too many stocks to look up! Try again with fewer than 10"])
        else:
            for word in tline:
                outputs.append([data['channel'], find_quote(word)])

def find_quote(word):
    """Given an individual symbol, 
    find and return the corresponding financial data

    word -- the symbol for which you're finding the data (ex. "GOOG")
    """
    cleanword=re.sub('[@<>]', '', word)
    share = Share(cleanword)
    price = share.get_price()
    if price != None:
        
        # Extract data
        day_high = share.get_days_high()
        day_low = share.get_days_low()
        market_cap = share.get_market_cap()
        year_high = share.get_year_high()
        year_low = share.get_year_low()
        yoy = get_YoY(share)
        
        output_string = ('*Stock*: \'{}\' \n*Current Price*: ${} \n*Day Range*: '
        '${} - ${} \n*52 Wk Range*: ${} - ${} \n*YoY Change*: {}\n*Market Cap*: ' 
        '${}').format(word.upper(), str(price), str(day_low), str(day_high), 
                      str(year_low), str(year_high), str(yoy), str(market_cap))
    else:
        output_string = "Can't find a stock with the symbol \'" + cleanword.upper() + "\'"
    return output_string
                               
def get_YoY(share):
    """For a given stock, return the year-over-year change in stock price

    share -- the Yahoo Finance Share object for the stock in question
    """
    
    # Get old closes from Yahoo
    year_ago_start = "{:%Y-%m-%d}".format(dt.date.today() - dt.timedelta(days=365))
    year_ago_end = "{:%Y-%m-%d}".format(dt.date.today() - dt.timedelta(days=363))

    old_list = share.get_historical(year_ago_start, year_ago_end)
    if len(old_list) == 0:
        return "NA"
    
    # Get close from a year ago, or if that was a weekend, the next most recent close
    old = float(old_list[-1]['Close'])    
    new = float(share.get_price())
        
    # Calculate YoY
    delta = int(round((new - old) / old * 100,0))
    if delta > 0:
        yoy = "+" + str(delta) + "%"
    else:
        yoy = str(delta) + "%"
    return yoy