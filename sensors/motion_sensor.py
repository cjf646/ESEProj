from gpiozero import MotionSensor 
from datetime import datetime
import time

pir = MotionSensor(17) 
counter = 0

while True:
  pir.wait_for_motion()
  if (pir):
    counter += 1
    print(counter) 
  now1 = (datetime.now())
  tstamp1 = "{0:%Y}-{0:%m}-{0:%d}_{0:%H}.{0:%M}.{0:%S}".format(now1) 
  filename = tstamp1 + "motion log.txt"
  file = open("motion_log.txt", "a")
  file.write("Motion detected " + tstamp1 + "\n")
  pir.wait_for_no_motion()
  print("STOPPED")
  now2 = (datetime.now())
  tstamp2 = "{0:%Y}-{0:%m}-{0:%d}_{0:%H}.{0:%M}.{0:%S}".format(now2) 
  file = open("motion_log.txt", "a")
  file.write("Motion stopped " + tstamp2 + "\n")
  time.sleep(1) 
file.close()
