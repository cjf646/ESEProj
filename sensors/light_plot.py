import numpy as np
import matplotlib.pyplot as plt
import time
from datetime import datetime

data = np.loadtxt('light_log.txt')
now = (datetime.now())
tstamp = "{0:%Y},{0:%m},{0:%d}".format(now)

x = data[:, 1]
y = data[:, 0]
plt.title('Light Graph for ' + tstamp)
plt.ylabel('Light Threshold')
plt.xlabel('Time')
plt.plot(x, y, 'r--')
plt.show()
plt.savefig(tstamp + '_light.png')
