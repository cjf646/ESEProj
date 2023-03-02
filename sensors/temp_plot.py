import numpy as np
import matplotlib.pyplot as plt
import time
from datetime import datetime

data = np.loadtxt('temp-humid_log.txt')
now = (datetime.now())
tstamp = "{0:%Y},{0:%m},{0:%d}".format(now)

x = data[:, 2]
y = data[:, 0]
plt.title('Temperature Graph for ' + tstamp)
plt.ylabel('Temperature (deg C)')
plt.xlabel('Time')
plt.plot(x, y, 'r--')
plt.savefig(tstamp + '_temp.png')
plt.show()
