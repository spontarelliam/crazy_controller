#!/usr/bin/env python
# RVA Makerfest RetroPi controller
# Adam, Justin
 
import RPi.GPIO as GPIO, time, os
import random

light_sensor_pin = 18
servo_pin = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, 50)
 
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
    return reading


def move_servo():
    x = random.randrange(100)
    pwm.start(x)
    time.sleep(0.1)
    

def main():
    while True:                                     
        read_light_sensor(light_sensor_pin)     # Read RC timing using pin #18
        move_servo()
    
if __name__ == '__main__':
    main()
