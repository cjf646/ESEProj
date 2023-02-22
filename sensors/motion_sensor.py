from gpiozero import MotionSensor 
from datetime import datetime
import time

pir = MotionSensor(17) 
counter = 0
plot = "1"
zero = "0"

while True: 
  now = (datetime.now())
  tstamp = "{0:%H}{0:%M}{0:%S}".format(now) 
  if pir.motion_detected:
        counter += 1
        print("Motion detected")
        with open("motion_log.txt", "a") as file:
            file.write(plot + " " + tstamp + "\n")
            time.sleep(1)
  else:
        print("No motion detected")
        with open("motion_log.txt", "a") as file:
            file.write(zero + " " + tstamp + "\n")
            time.sleep(1)
file.close()
