#!/usr/bin/python
#
# Blink 2 LEDs twice
#
import time
import RPi.GPIO as GPIO

# set to Broadcom pin numbering scheme
GPIO.setmode(GPIO.BCM)
# we wil use GPIO pin 17 and 27 to turn leds on/off
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

print "First blink"

#Turn LEDs on
GPIO.output(17,GPIO.HIGH)
GPIO.output(27,GPIO.HIGH)
time.sleep(1)

#Turn LEDs off
GPIO.output(17,GPIO.LOW)
GPIO.output(27,GPIO.LOW)
time.sleep(1)

print "Second blink"
#Turn LEDs on
GPIO.output(17,GPIO.HIGH)
GPIO.output(27,GPIO.HIGH)
time.sleep(1)

#Turn LEDs off
GPIO.output(17,GPIO.LOW)
GPIO.output(27,GPIO.LOW)
GPIO.cleanup()

print "Done"
