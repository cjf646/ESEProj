import time
import RPi.GPIO as GPIO
import sys
import subprocess

# Import LCD library
from RPLCD import i2c

lcdmode = 'i2c'
cols = 20
rows = 4
charmap = 'A00'
i2c_expander = 'PCF8574'

# Generally 27 is the address;Find yours using: i2cdetect -y 1
address = 0x27
port = 1 # 0 on an older Raspberry Pi

# Initialise the LCD
lcd = i2c.CharLCD(i2c_expander, address, port=port, charmap=charmap,
                  cols=cols, rows=rows)

subprocess.call(['/home/cjf646/run_again.sh'])
#(crontab -e) @reboot python3 /home/cjf646/Desktop/ESE_Final_Project/lcdTest.py &

    
    
