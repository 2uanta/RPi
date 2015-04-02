#!/usr/bin/python
#
# Turn 2 LEDs on
#
import RPi.GPIO as GPIO

# set to Broadcom pin numbering scheme
GPIO.setmode(GPIO.BCM)
# we will use GPIO pin 17 and 27 to turn leds on/off
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
# We will turn the lights on
print "Lights on"
# by applying high voltage
GPIO.output(17,GPIO.HIGH)
GPIO.output(27,GPIO.HIGH)

print "Done"
