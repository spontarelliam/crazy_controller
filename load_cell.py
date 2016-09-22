import smbus
from time import sleep

bus = smbus.SMBus(1)

val = 0
while True:
	sleep(0.1)
	try:
		val = (0.75 * val) + (0.25 * bus.read_byte_data(0x28, 0x80))
		if val > 80:
			print "Right"
		elif val < 40:
			print "Left"
		else:
			print "Center"
	except:
		pass
