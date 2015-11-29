# stock-quote-slackbot
A slackbot that retrieves stock quotes from Yahoo Finance given a ticker symbol in Slack. Pretty simple!

## Background
Stockbot is Slack's Python-based [real-time messaging bot](https://github.com/slackhq/python-rtmbot) wrapped around Łukasz Banasiak's [Python wrapper](https://github.com/lukaszbanasiak/yahoo-finance/) for the Yahoo Finance API.

### Dependencies
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
 Go to Slack integrations, make a new Slackbot, and grab the token. You'll get to choose your bot's name and icon.
 Also, you'll pick a trigger word in the rtmbot.conf file.

  ````
  cp example-config/rtmbot.conf .
  vi rtmbot.conf
  SLACK_TOKEN: "xoxb-11111111111-222222222222222"
  TRIGGER_WORD: "quote"
  
  ````

4. Run it! (You've got to keep it running as long as you'd it to respond; something like [nohup](http://linux.die.net/man/1/nohup) might be helpful.)

````
  python rtmbot.py
````

### Example Usage

.. code:: python

    >>> quote GOOG YHOO
    The current stock price for 'GOOG' is: $750.26
    The current stock price for 'YHOO' is: $32.94


