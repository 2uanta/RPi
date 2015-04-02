#!/usr/bin/python
#
# Deteck button pressed
# Use GPIO.wait_for_edge function to detect voltage change
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
    while True:
        print ("\nWaiting for you to press a button")
        # PIN 10 HIGH -> button not pressed, LOW -> button pressed
        # Wait for PIN 10 LOW (button pressed)
        try: 
            GPIO.wait_for_edge(10,GPIO.FALLING)
	    print("==> Button Pressed")
            os.system('date')
        except KeyboardInterrupt:
            print "Keyboard Interrupt!"
            print "Done"
            GPIO.cleanup()
            exit

        # Wait for PIN 10 HIGH (button released)
        GPIO.wait_for_edge(10,GPIO.RISING)
	print("==> Button Released")
        os.system('date')
    time.sleep(1)

except KeyboardInterrupt:
    print "Keyboard Interrupt!"
    print "Done"
    GPIO.cleanup()

