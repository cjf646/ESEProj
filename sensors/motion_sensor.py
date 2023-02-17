from gpiozero import MotionSensor 
from datetime import datetime
import time

pir = MotionSensor(17) 
counter = 0
plot = "1"
zero = "0"

while True:
  pir.wait_for_motion()
  if (pir):
    counter += 1
    print(counter) 
  now = (datetime.now())
  tstamp = "{0:%H}{0:%M}{0:%S}".format(now) 
  file = open("motion_log.txt", "a")
  file.write(plot + " " + tstamp + "\n")
  pir.wait_for_no_motion()
  print("STOPPED")
  if (pir):
    file.write(zero + " " + tstamp + "\n")
  time.sleep(1) 
file.close()
