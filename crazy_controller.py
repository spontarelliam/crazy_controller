#!/usr/bin/env python
 
# Example for RC timing reading for Raspberry Pi
# Must be used with GPIO 0.3.1a or later - earlier verions
# are not fast enough!
 
import RPi.GPIO as GPIO, time, os
import random

DEBUG = 1
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12, 50)
pwm.start(5)
 
def RCtime (RCpin):
        reading = 0
        GPIO.setup(RCpin, GPIO.OUT)
        GPIO.output(RCpin, GPIO.LOW)
        time.sleep(0.1)
 
        GPIO.setup(RCpin, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        
        while (GPIO.input(RCpin) == GPIO.LOW):
                reading += 1

        if reading < 300:
                print('hit')
        return reading

 
while True:                                     
        RCtime(18)     # Read RC timing using pin #18
        x = random.randrange(100)
	pwm.start(x)
	time.sleep(0.1)

