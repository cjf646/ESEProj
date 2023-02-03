from datetime import datetime
import RP1.GPIO as GPIO 
import time

readPIN 14
counter 0
value 0
conv 0

GPIO.setwarnings (False)
GPIO.setmode (GPIO.BCM) 
GPIO.setup(readPIN, GPIO.IN)
GPIO.setwarnings(True)

try:
  while True:
    value = str(GPIO.input (readPIN))
    conv = int(value)
    if(conv == 1): 
      counter += 1
      print(counter)
    now = (datetime.now())
    tstamp = "{0:%Y}-{0:%m}-{0:%d}_{0:%H}.{0:%M}.{0:%S}".format(now)
    filename = tstamp + "light_log.txt"
    file = open("light_log.txt", "a")
    file.write("Light detected " + tstamp + "\n")
    time.sleep(1) 
  file.close()
except KeyboardInterrupt:
  print('interuppted')
  GPIO.cleanup()
