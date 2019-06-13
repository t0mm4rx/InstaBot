# InstaBot

## Project presentation
This project is a python Instagram bot that follow and like everything.
The goal of this project is to get the maximum number followers without posting anything.

Instagram followers limit is 160/hour ! So don't go to fast or you'll get banned.

Tested and developped on Arch Linux with Firefox webdrivers.

## Dependencies
The only dependency is Selenium :
```
sudo pip install selenium
```
You also need to install Selenium webdrivers, I tested with Firefox only.

## How does it work ?
First create a .json file containing your account creds :
```json
{
  "username": "your_username",
  "password": "your_password"
}
```
Next, import and instantiate the Bot class :
```python
from Bot import Bot

"""
  The first param is a HTTP proxy, leave 127.0.0.1 if you don't want one.
  The second one is the name of the json file that contains your creditentials.   
"""

bot = Bot('127.0.0.1', 'creds.json')

# The bot will go to fashion hashtag page and will like and follow 160 posts
bot.browse_hashtag('fashion')

# The bot will be in the "suggested friends" page and subscribe to everyone
bot.browse_suggested()

# This function will add the current number of followers and followed in the stats.json file
# This function is called after every browse_* function, so you don't need to use it manually
bot.save_stats()

```
