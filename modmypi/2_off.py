#!/usr/bin/python
#
# Turn 2 LEDs off
#
import RPi.GPIO as GPIO

# set to Broadcom pin numbering scheme
GPIO.setmode(GPIO.BCM)
# we wil use GPIO pin 17 and 27 to turn leds on/off
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
# We will turn the lights off
print "Lights off"
# by applying low voltage
GPIO.output(17,GPIO.LOW)
GPIO.output(27,GPIO.LOW)
GPIO.cleanup()

print "Done"

