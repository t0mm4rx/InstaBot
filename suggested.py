import time
import datetime
from Bot import Bot

bot = Bot('178.170.117.29', 'creditentials.json')
time.sleep(60)
while True:
    a = 0
    while (a < 130):
        a += bot.browse_suggested()
    print("[{}] Followed {} : now waiting for one hour".format(bot.get_date()
, a))
    time.sleep(60 * 60)
