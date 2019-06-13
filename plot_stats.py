import json
import matplotlib.pyplot as plt
import datetime

history = json.loads(open('stats.json').read())

x = []
y1 = []
y2 = []
for h in history:
    x.append(h['date'])
    y1.append(h['followers'])
    y2.append(h['followed'])

plt.plot(x, y1, label="Followers")
plt.plot(x, y2, label="Followed")
plt.legend()
plt.savefig("./graphs/graph_{}.png".format(datetime.datetime.now().strftime("%d-%m-%Y_%H:%M")))
plt.show()
