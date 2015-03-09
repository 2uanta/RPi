# raspberry pi project
# Reference: Raspberry Pi Cookbook - Chapter 9
# Note: RGB LED (4-pins)
#   pin 1 RED LED
#   pin 2 GND
#   pin 3 GREEN LED
#   pin 4 BLUE LED
# Wiring diagram
# 	GPIO pin 18 --> resistor --> pin 1 RGB LED
#	GND         ---------------> pin 2 RGB LED
# 	GPIO pin 23 --> resistor --> pin 3 RGB LED
# 	GPIO pin 24 --> resistor --> pin 4 RGB LED
# Description
#	Light up the RGB LED with different colors

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

while True:
    pwnRed = GPIO.PWM(18, 500)
    pwnRed.start(100)
    sleep(500)
    
    pwnGreen = GPIO.PWM(23, 500)
    pwnGreen.start(100)
    sleep(500)
    
    pwnBlue = GPIO.PWM(24, 500)
    pwnBlue.start(100)
    sleep(500)


