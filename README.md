# stock-quote-slackbot
A slackbot that retrieves stock quote information from Yahoo Finance given a ticker symbol in Slack.

## Background
Stockbot is Slack's Python-based [real-time messaging bot](https://github.com/slackhq/python-rtmbot) wrapped around Łukasz Banasiak's [Python wrapper](https://github.com/lukaszbanasiak/yahoo-finance/) for the Yahoo Finance API.

### Dependencies
* [numpy](https://pypi.python.org/pypi/numpy)
* [websocket-client](https://pypi.python.org/pypi/websocket-client/)
* [python-slackclient](https://pypi.python.org/pypi/slackclient)
* [yahoo-finance](https://pypi.python.org/pypi/yahoo-finance)

### Installation
1. Download stockbot

  ````
  git https://github.com/NosajGithub/stock-quote-slackbot.git
  cd stock-quote-slackbot
  ````

2. Install dependencies

  ````
  pip install -r requirements.txt
  ````

3. Configure rtmbot ([Slack instructions](https://api.slack.com/bot-users).) 
 Go to Slack integrations, make a new Slackbot, and grab the token. You get to choose your bot's name and icon.
 Also, pick a trigger word in the rtmbot.conf file.

  ````
  cp example-config/rtmbot.conf .
  vi rtmbot.conf
  SLACK_TOKEN: "xoxb-11111111111-222222222222222"
  TRIGGER_WORD: "quote"
  
  ````

4. Run it! (You've got to keep it running as long as you want to use it; something like [nohup](http://linux.die.net/man/1/nohup) might be helpful.)

````
  python rtmbot.py
````

### Usage

There are two ways to use stockbot. The first is to input the trigger word ('quote' by default) and one or more stock tickers. 
You'll get back a separate reply for each stock listed.  

The second usage is to enter the word 'range', a ticker symbol, and a start and end date. 
Stockbot will return the average stock price over that date range.  

### Example Usage  

    >>> quote GOOG YHOO
    Stock​: 'GOOG'
    Current Price​: $742.60
    Day Range​: $741.27 - $754.93
    52 Wk Range​: $486.23 - $762.71
    YoY Change​: +39%
    Market Cap​: $510.70B
     
    Stock​: 'YHOO'
    Current Price​: $33.81
    Day Range​: $32.85 - $33.83
    52 Wk Range​: $27.20 - $51.68
    YoY Change​: -33%
    Market Cap​: $31.93B
    
    >>> range yhoo 2014-11-30 2015-11-30
    The average price for 'YHOO' from 2014-11-30 to 2015-11-30 is: $40.41
    