#!/usr/bin/env python
import RPi.GPIO as GPIO
from time import sleep
import cgi
import cgitb; cgitb.enable(display=1, logdir=None, context=5, format="html")

GPIO.setmode(GPIO.BOARD)
 
Motor1A = 16
Motor1B = 18
Motor1E = 22
 
Motor2A = 19
Motor2B = 21
Motor2E = 23
  
print "Now stop"
GPIO.output(Motor1E,GPIO.LOW)
GPIO.output(Motor2E,GPIO.LOW)
 
GPIO.cleanup()
