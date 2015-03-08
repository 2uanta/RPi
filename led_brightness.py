# raspberry pi project
# Reference: Raspberry Pi Cookbook - Chapter 9
# Wiring diagram
# 	GPIO pin 18 --> 10K Ohm resistor
# 	10K Ohm resistor --> (+/anode longer pin) Red LED
# 	(-/cathode shorter pin) Red LED --> GND
# Description
# 	Change level of brightness of LED from 0 to 100

import RPi.GPIO as GPIO

led_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

pwm_led = GPIO.PWM(led_pin, 500)
pwm_led.start(100)

while True:
    duty_s = raw_input("Enter Brightness (0 to 100):")
    duty = int(duty_s)
    pwm_led.ChangeDutyCycle(duty)
