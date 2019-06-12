import time
from Bot import Bot

bot = Bot('178.170.117.29', 'creditentials.json')

while True:
    a = 0
    while (a < 100):
        a += bot.browse_suggested()
    time.sleep(60 * 60)
