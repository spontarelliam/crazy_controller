import time
import RPi.GPIO as GPIO
from subprocess import Popen, PIPE

RPM_SAMPLE_TIME_S = 1
HE_SENSOR_PIN = 2

GPIO.setmode( GPIO.BCM )
GPIO.setup( HE_SENSOR_PIN, GPIO.IN )

GPIO.add_event_detect( HE_SENSOR_PIN, GPIO.FALLING )

go = '''keydown Shift_L
key Y
keyup Shift_L
'''

def keypress(sequence):
    p = Popen(['xte'], stdin=PIPE)
    p.communicate(input=sequence)
        
def accelerate(cycles, rpm):
    """
    tap accelerate in proportion to the measured rpm
    """
    print(cycles)
    for i in range(cycles):
        keypress(go)

fTime = 0.0
iCycles = 0
fRPM = 0.0
while True:
    if GPIO.event_detected( HE_SENSOR_PIN ):
        iCycles += 1
    fDeltaTime = time.time() - fTime
    if fDeltaTime > RPM_SAMPLE_TIME_S:
        fRPM = (iCycles / fDeltaTime) * 60
        accelerate(iCycles, fRPM)
        iCycles = 0
        fTime = time.time()


