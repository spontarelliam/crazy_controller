import time
import RPi.GPIO as GPIO
from subprocess import Popen, PIPE
import os

RPM_SAMPLE_TIME_S = 1
HE_SENSOR_PIN = 2
G_PIN = 4

GPIO.setmode( GPIO.BCM )
GPIO.setup( HE_SENSOR_PIN, GPIO.IN )
GPIO.setup( G_PIN, GPIO.OUT )
GPIO.output(G_PIN, 1)

GPIO.add_event_detect( HE_SENSOR_PIN, GPIO.FALLING )
        
def accelerate(cycles, rpm):
    """
    tap accelerate in proportion to the measured rpm
    """
    for i in range(cycles):
        GPIO.output(G_PIN, 0)
        time.sleep(0.4)
        GPIO.output(G_PIN, 1)

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


