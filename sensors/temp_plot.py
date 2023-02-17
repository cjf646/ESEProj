import numpy as np
import matplotlib.pyplot as plt
import time
from datetime import datetime

data = np.loadtxt('temp-humid_log.txt')
now = (datetime.now())
tstamp = "{0:%Y}_{0:%m}_{0:%d}".format(now)

x = data[:, 2]
y = data[:, 0]
plt.title('Temperature Graph for ' + tstamp)
plt.ylabl('Temperature (deg C)')
plt.xlabel('Time')
plt.plot(x, y, 'r--')
plt.show()
plt.savefig(tstamp + '_temp.png')
