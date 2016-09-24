import time
import RPi.GPIO as GPIO
from subprocess import Popen, PIPE
import os
from multiprocessing import Process

RPM_SAMPLE_TIME_S = 1.0
HE_SENSOR_PIN = 13
G_PIN = 4

GPIO.setwarnings(False)
GPIO.setmode( GPIO.BCM )
GPIO.setup(HE_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(G_PIN, GPIO.OUT)
GPIO.output(G_PIN, 1)

GPIO.add_event_detect( HE_SENSOR_PIN, GPIO.FALLING )

def accelerate(cycles, rpm):
    """
    tap accelerate in proportion to the measured rpm
    6 cycles is realistic max
    """
    cycles = min(cycles, 6)
    delay = (cycles / 6) * RPM_SAMPLE_TIME_S
    GPIO.output(G_PIN, 0)
    time.sleep(delay)
    GPIO.output(G_PIN, 1)

fTime = time.time()
iCycles = 0
fRPM = 0.0
while True:
    detect = GPIO.event_detected(HE_SENSOR_PIN)
    if detect:
        iCycles += 1
        fDeltaTime = time.time() - fTime
        if fDeltaTime > RPM_SAMPLE_TIME_S:
            fRPM = (iCycles / fDeltaTime) * 60
            p = Process(target=accelerate, args=(iCycles,fRPM))
            p.start()
            iCycles = 0
            fTime = time.time()
