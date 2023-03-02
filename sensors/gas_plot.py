import numpy as np
import matplotlib.pyplot as plt
import time
from datetime import datetime

data = np.loadtxt('gas_log.txt')
now = (datetime.now())
tstamp = "{0:%Y},{0:%m},{0:%d}".format(now)

x = []
for timestamp in data[:, 3]:
    time_str = str(int(timestamp))
    formatted_time_str = ':'.join([time_str[i:i+2] for i in range(0, len(time_str), 2)])
    x.append(formatted_time_str)
y1 = data[:, 0]
y2 = data[:, 1]
y3 = data[:, 2]
plt.title('Gas Graph for ' + tstamp)
plt.ylabel('Concentration (ppm)')
plt.xlabel('Time')
plt.plot(x, y1, 'r--')
plt.plot(x, y2, 'r--')
plt.plot(x, y3, 'r--')
plt.xticks(rotation=45, ha='right')
plt.gcf().set_size_inches(19.20, 10.80)
plt.savefig(tstamp + '_gas.png', dpi=100)
