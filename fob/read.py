#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
  id, text = reader.read()
  print(id)
  if(id == 704238721961)
    print("CORRECT FOB")
  else:
    print("INVALID FOB")

  print(text)
   
finally:
  GPIO.cleanup()
