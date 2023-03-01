from datetime import datetime
import RPi.GPIO as GPIO 
import time

readPIN = 14
counter = 0
value = 0
conv = 0

GPIO.setwarnings (False)
GPIO.setmode (GPIO.BCM) 
GPIO.setup(readPIN, GPIO.IN)
GPIO.setwarnings(True)

try:
  while True:
    value = str(GPIO.input(readPIN))
    conv = int(value)
    if(conv == 1): 
      counter += 1
      print(counter)
      log_value = '1'
    else:
      log_value = '0'
    now = datetime.now()
    tstamp = "{0:%H}{0:%M}{0:%S}".format(now)
    file = open("light_log.txt", "a")
    file.write(log_value + " " + tstamp + "\n")
    time.sleep(1) 
finally:
  GPIO.cleanup()
