#!/usr/bin/python
#
# Deteck button pressed
# Use GPIO.wait_for_edge function to detect voltage change
# And create and event with callnback function
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

def f(channel):
    print("==> Button Pressed ")
    os.system('date')

print("------------------")
print(" Button + GPIO ")
print("------------------")

print "Current pin 10 status: ", GPIO.input(10)

GPIO.add_event_detect(10,GPIO.FALLING,callback=f, bouncetime=50)

try: 
    # initialize a previous input variable to 0 (button not pressed)
    while True:
        next
    time.sleep(1)

except KeyboardInterrupt:
    print "Keyboard Interrupt!"
    print "Done"
    GPIO.remove_event_detect(10)
    GPIO.cleanup()

