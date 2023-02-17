import Adafruit_DHT 
import time
from datetime import datetime

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
counter = 0
sum_temp = 0.0
sum_humid = 0.0

while True:
  humidity, temperature = Adafruit_DHT.read(DHT SENSOR, DHT_PIN)
  if humidity is not None and temperature is not None:
    print("Temperature={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
    temp = str(temperature) 
    humid = str(humidity)
    conv_temp = float(temp) 
    conv_humid = float(humid) 
    file = open("temp-humid_log.txt", "a") 
    file.write(temp + " ")
    sum_temp = sum_temp + conv_temp 
    sum_humid = sum_humid + conv_humid
    counter += 1
    average_temp = sum_temp/counter 
    average_humid = sum_humid/counter
    print("Average Temperature={0:0.1f}C Average Humidity={1:0.1f}%".format(average temp, average_humid))
    now = (datetime.now())
    tstamp = "{0:%H}{0:%M}{0:%S}".format(now)
    file.write(tstamp + "\n")
  time.sleep(1);
file.close()
