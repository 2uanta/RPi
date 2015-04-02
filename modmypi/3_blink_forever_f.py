#!/usr/bin/python
#
# Blink 2 LEDs forwever until keyboard interrupt (CTL-C)
#
import time
import RPi.GPIO as GPIO

# set to Broadcom pin numbering scheme
GPIO.setmode(GPIO.BCM)
# we will use GPIO pin 17 and 27 to turn leds on/off
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

def led_on(pin):
    GPIO.output(pin,GPIO.HIGH)
def led_off(pin):
    GPIO.output(pin,GPIO.LOW)

try:
    while 1:
        print "On"
        #Turn LEDs on
        led_on(17)
        led_off(27)
        time.sleep(1)

        print "Off"
        #Turn LEDs off
        led_off(17)
        led_on(27)
        time.sleep(1)

except KeyboardInterrupt: 
	print "Keyboard Interrupt!"
	print "Done"
	GPIO.cleanup()
