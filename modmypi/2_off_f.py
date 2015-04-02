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
# We will turn the lights off
print "Lights off"

def led_off(pin):
    GPIO.output(pin,GPIO.LOW)

# by applying high voltage
led_off(17)
led_off(27)

print "Done"
