import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import time

i2c = busio.I2C(board.SCL, board.SDA)

ads = ADS.ADS1015(i2c)

channels = [AnalogIn(ads, ADS.P0), 
            AnalogIn(ads, ADS.P1),
            AnalogIn(ads, ADS.P2)]

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

    print('LPG Concentration: {:.2f} ppm'.format(lpg_conc))
    print('CO2 Concentration: {:.2f} ppm'.format(co2_conc))
    print('Smoke Concentration: {:.2f} ppm'.format(smoke_conc))

    time.sleep(1)
