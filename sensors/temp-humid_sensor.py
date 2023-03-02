import time
import board
import adafruit_dht
from datetime import datetime

dhtDevice = adafruit_dht.DHT11(board.D4)
counter = 0
sum_temp = 0.0
sum_humid = 0.0

while True:
    try:
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print("Temp: {:.1f} C    Humidity: {}% ".format(temperature_c, humidity))
        temp = str(temperature_c) 
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
        print("Average Temperature={0:0.1f}C Average Humidity={1:0.1f}%".format(average_temp, average_humid))
        now = (datetime.now())
        tstamp = "{0:%H}{0:%M}{0:%S}".format(now)
        file.write(tstamp + "\n")

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)
file.close()
