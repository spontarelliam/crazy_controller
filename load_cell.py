import smbus
from time import sleep
import RPi.GPIO as GPIO, time, os

bus = smbus.SMBus(1)

D_PIN = 17
S_PIN = 27

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(D_PIN, GPIO.OUT)
GPIO.setup(S_PIN, GPIO.OUT)

val = 0
while True:
	sleep(0.1)
	try:
		val = (0.5 * val) + (0.25 * bus.read_byte_data(0x28, 0x80))
		if val > 60:
                        GPIO.output(D_PIN, 0)
                        time.sleep(0.1)
                        GPIO.output(D_PIN, 1)
		elif val < 20:
                        GPIO.output(S_PIN, 0)
                        time.sleep(0.1)
                        GPIO.output(S_PIN, 1)
		else:
                        # center
                        pass
	except:
		pass
