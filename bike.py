import time

import RPi.GPIO as GPIO

RPM_SAMPLE_TIME_S = 1
HE_SENSOR_PIN = 2

GPIO.setmode( GPIO.BCM )
GPIO.setup( HE_SENSOR_PIN, GPIO.IN )

GPIO.add_event_detect( HE_SENSOR_PIN, GPIO.FALLING )

iCycles = 0
fTime = 0.0
fRPM = 0.0
while True:
    if GPIO.event_detected( HE_SENSOR_PIN ):
        iCycles += 1

    fDeltaTime = time.time() - fTime
    if fDeltaTime > RPM_SAMPLE_TIME_S:
        fRPM = (iCycles / fDeltaTime) * 60
        iCycles = 0
        fTime = time.time()

        #DEBUG
        print( fRPM )
        #DEBUG

