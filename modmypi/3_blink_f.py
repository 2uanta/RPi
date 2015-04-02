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

def led_on(pin):
    GPIO.output(pin,GPIO.HIGH)
def led_off(pin):
    GPIO.output(pin,GPIO.LOW)

#Turn LEDs on
led_on(17)
led_on(27)
time.sleep(1)

#Turn LEDs off
led_off(17)
led_off(27)
time.sleep(1)

print "Second blink"
#Turn LEDs on
led_on(17)
led_on(27)
time.sleep(1)

#Turn LEDs off
led_off(17)
led_off(27)
GPIO.cleanup()

print "Done"
