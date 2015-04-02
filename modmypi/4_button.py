#!/usr/bin/python
#
# Deteck button pressed
# Use prev_input variable to remember the previous state of the pin
#
import os
import time
import RPi.GPIO as GPIO
# set to Broadcom pin numbering scheme
GPIO.setmode(GPIO.BCM)

# Use GPIO 10 which also is SPI MOSI pin to detect button pressed

# It is attached to a pull-up resistor so the buzzer is connected to GND
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# If it is attached to a pull-up resistor so the buzzer is connected to 3.3V
# GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print("------------------")
print(" Button + GPIO ")
print("------------------")

print "Current pin 10 status: ", GPIO.input(10)
try: 
    # initialize a previous input variable to 0 (button not pressed)
    prev_input = 0
    while True:
        # 
        # take a reading from GPIO pin 10
        input = GPIO.input(10)
        # if the last reading was low and this one high, then button pressed
        if ((not prev_input) and input):
            os.system('clear')
	    print("Button Pressed")
            os.system('date')
            # slight pause to debounce
            time.sleep(0.05)
            print ("Waiting for you to press a button")
        prev_input = input
    time.sleep(1)

except KeyboardInterrupt:
    print "Keyboard Interrupt!"
    print "Done"
    GPIO.cleanup()

