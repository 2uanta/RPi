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

def led_on(pin):
    GPIO.output(pin,GPIO.HIGH)

# by applying high voltage
led_on(17)
led_on(27)

print "Done"
