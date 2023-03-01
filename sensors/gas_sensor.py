import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import time

i2c = busio.I2C(board.SCL, board.SDA)

ads = ADS.ADS1015(i2c)

channels = [AnalogIn(ads, ADS.P0), AnalogIn(ads, ADS.P1), AnalogIn(ads, ADS.P2)]

counter = 0

lpg_sum = 0
co2_sum = 0
smoke_sum = 0

ZERO_LPG = 500
ZERO_CO2 = 500
ZERO_SMOKE = 500

while True:
    lpg = channels[0].value
    co2 = channels[1].value
    smoke = channels[2].value

    lpg_conc = (lpg - ZERO_LPG) / 10.0
    co2_conc = (co2 - ZERO_CO2) / 10.0
    smoke_conc = (smoke - ZERO_SMOKE) / 10.0
            
    counter += 1

    lpg_sum = lpg_sum + lpg_conc
    co2_sum = co2_sum + co2_conc
    smoke_sum = smoke_sum + smoke_conc

    average_lpg = lpg_sum/counter        
    average_co2 = co2_sum/counter          
    average_lpg = smoke_sum/counter 
            
    lpg_conv = str(lpg_conc)
    co2_conv = str(co2_conc)
    smoke_conv = str(smoke_conc)

    now = (datetime.now())
    tstamp = "{0:%H}{0:%M}{0:%S}".format(now)

    file = open("gas_log.txt", "a")
    file.write(lpg_conv + " ") 
    file.write(co2_conv + " ") 
    file.write(smoke_conv + " ")    
    file.write(tstamp + "\n")         

    print('LPG Concentration: {:.2f} ppm'.format(lpg_conc))
    print('CO2 Concentration: {:.2f} ppm'.format(co2_conc))
    print('Smoke Concentration: {:.2f} ppm'.format(smoke_conc))
    print('Average LPG Concentration: {:.2f} ppm'.format(average_lpg))
    print('Average CO2 Concentration: {:.2f} ppm'.format(average_co2))
    print('Average Smoke Concentration: {:.2f} ppm'.format(average_smoke))
    print('\n')

    time.sleep(10)
