import numpy as np
import matplotlib.pyplot as plt
import time
from datetime import datetime

data = np.loadtxt('gas_log.txt')
now = (datetime.now())
tstamp = "{0:%Y},{0:%m},{0:%d}".format(now)

x = data[:, 3]
y1 = data[:, 0]
y2 = data[:, 1]
y3 = data[:, 2]
plt.title('Gas Graph for ' + tstamp)
plt.ylabel('Concentration (ppm)')
plt.xlabel('Time')
plt.plot(x, y1, 'r--')
plt.plot(x, y2, 'r--')
plt.plot(x, y3, 'r--')
plt.savefig(tstamp + '_gas.png'
plt.show()
