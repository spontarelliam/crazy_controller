import smbus
from time import sleep

bus = smbus.SMBus(1)

D_PIN = 17
S_PIN = 27

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(D_PIN, GPIO.OUT)
GPIO.setup(S_PIN, GPIO.OUT )

val = 0
while True:
	sleep(0.1)
	try:
		val = (0.75 * val) + (0.25 * bus.read_byte_data(0x28, 0x80))
		if val > 80:
			print "Right"
                        GPIO.output(D_PIN, 0)
                        time.sleep(0.1)
                        GPIO.output(D_PIN, 1)
		elif val < 40:
			print "Left"
                        GPIO.output(S_PIN, 0)
                        time.sleep(0.1)
                        GPIO.output(S_PIN, 1)
		else:
			print "Center"
	except:
		pass
