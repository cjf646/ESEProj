import numpy as np
import matplotlib.pyplot as plt
import time
from datetime import datetime

data = np.loadtxt('motion_log.txt')
now = (datetime.now())
tstamp = "{0:%Y}_{0:%m}_{0:%d}".format(now)

x = data[:, 1]
y = data[:, 0]
plt.title('Motion Graph for ' + tstamp)
plt.ylabl('Movement')
plt.xlabel('Time')
plt.plot(x, y, 'r--')
plt.show()
plt.savefig(tstamp + '_motion.png')