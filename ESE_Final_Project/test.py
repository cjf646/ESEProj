import time
import RPi.GPIO as GPIO
# Import LCD library
from RPLCD import i2c

import subprocess
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
lcd.close(clear=True)
lcd.write_string('LOADING.....')
lcd.crlf()
lcd.write_string('PLEASE WAIT')
lcd.crlf()
time.sleep(10)
lcd.close(clear=True)
subprocess.call(['/home/cjf646/run_again.sh'])

