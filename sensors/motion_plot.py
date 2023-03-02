import numpy as np
import matplotlib.pyplot as plt
import time
from datetime import datetime

data = np.loadtxt('motion_log.txt')
now = (datetime.now())
tstamp = "{0:%Y},{0:%m},{0:%d}".format(now)

x = []
for timestamp in data[:, 1]:
    time_str = str(int(timestamp))
    formatted_time_str = ':'.join([time_str[i:i+2] for i in range(0, len(time_str), 2)])
    x.append(formatted_time_str)
y = data[:, 0]
plt.title('Motion Graph for ' + tstamp)
plt.ylabel('Movement')
plt.xlabel('Time')
plt.plot(x, y, 'r--')
plt.xticks(rotation=45, ha='right')
plt.savefig(tstamp + '_motion.png')
plt.show()
