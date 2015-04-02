#!/usr/bin/python
#
# gather user's choice to light up a led
#
import os
import time
import RPi.GPIO as GPIO
# set to Broadcom pin numbering scheme
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
# we will use GPIO pin 17 and 27 to turn leds on/off
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.output(17,GPIO.LOW)
GPIO.output(27,GPIO.LOW)

#Setup variables for user input
led_choice = 0
count = 0

os.system('clear')

try:
    print "Which LED would you like to blink"
    print "1: Red?"
    print "2: Blue?"

    led_choice = input("Choose your option: ")

    if led_choice == 1:
    	os.system('clear')
    	print "You picked the Red LED"
    	count = input("How many times would you like it to blink?: ")
    	while count > 0:
		print count
    		GPIO.output(17,GPIO.HIGH)
    		time.sleep(1)
    		GPIO.output(17,GPIO.LOW)
    		time.sleep(1)
    		count = count - 1
    		
    if led_choice == 2:
    	os.system('clear')
    	print "You picked the Blue LED"
    	count = input("How many times would you like it to blink?: ")
    	while count > 0:
		print count
    		GPIO.output(27,GPIO.HIGH)
    		time.sleep(1)
    		GPIO.output(27,GPIO.LOW)
    		time.sleep(1)
    		count = count - 1
    GPIO.cleanup()

except KeyboardInterrupt:
    print "\nKeyboard Interrupt!"
    print "Done"
    GPIO.cleanup()
