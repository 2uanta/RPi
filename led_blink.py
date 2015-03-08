# raspberry pi project
# Reference: Raspberry Pi Cookbook - Chapter 9
# Wiring diagram
# 	GPIO pin 18 --> 10K Ohm resistor
# 	10K Ohm resistor --> (+/anode longer pin) Red LED
# 	(-/cathode shorter pin) Red LED --> GND
# Description
#	Turn LED on/off by outputting on GPIO port 18
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

while (True):
    GPIO.output(18, True)
    time.sleep(0.5)
    GPIO.output(18, False)
    time.sleep(0.5)
