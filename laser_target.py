#!/usr/bin/env python
# RVA Makerfest RetroPi controller
# Laser target button
# Adam
 
import RPi.GPIO as GPIO, time, os
import random
from subprocess import Popen, PIPE

light_sensor_pin = 18
servo_pin = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, 50)

up = '''keydown Shift_L
key H
keyup Shift_L
'''

down = '''keydown Shift_L
key J
keyup Shift_L
'''

left = '''keydown Shift_L
key K
keyup Shift_L
'''

right = '''keydown Shift_L
key L
keyup Shift_L
'''

accelerate = '''keydown Shift_L
key Y
keyup Shift_L
'''

fire = '''keydown Shift_L
key U
keyup Shift_L
'''

def keypress(sequence):
        p = Popen(['xte'], stdin=PIPE)
        p.communicate(input=sequence)

def read_light_sensor (RCpin):
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.1)
 
    GPIO.setup(RCpin, GPIO.IN)
    # This takes about 1 millisecond per loop cycle
        
    while (GPIO.input(RCpin) == GPIO.LOW):
        reading += 1

    if reading < 300:
        print('laser hit')
        keypress(fire)

def move_servo():
    x = random.randrange(100)
    pwm.start(x)
    time.sleep(0.1)

def main():
    while True:                                     
        read_light_sensor(light_sensor_pin)
        move_servo()
    
if __name__ == '__main__':
    main()
