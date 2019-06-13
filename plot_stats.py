import json
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.dates import DateFormatter
import datetime

history = json.loads(open('stats.json').read())

dates = []
x_label = []
y1 = []
y2 = []
for h in history:
    d = datetime.datetime.strptime(h['date'], "%d/%m/%Y %H:%M")
    dates.append(d)
    y1.append(h['followers'])
    y2.append(h['followed'] / 10)

x = matplotlib.dates.date2num(dates)
plt.plot(x, y1, label="Followers")
plt.plot(x, y2, label="Followed * 1/10")

myFmt = DateFormatter('%d/%m %Hh')
plt.gca().xaxis.set_major_formatter(myFmt)

plt.legend()
plt.savefig("./graphs/graph_{}.png".format(datetime.datetime.now().strftime("%d-%m-%Y_%H:%M")))
plt.show()
