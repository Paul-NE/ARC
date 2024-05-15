# https://www.theengineeringprojects.com/2023/06/how-to-interface-mq-2-gas-sensor-with-raspberry-pi-4.html
# gass pins
11
0
6
19

import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(19,GPIO.IN)
GPIO.setup(11,GPIO.IN)
GPIO.setup(6,GPIO.IN)

while True:
    sensor_state_19=GPIO.input(19)
    sensor_state_11=GPIO.input(11)
    sensor_state_6=GPIO.input(6)
    if sensor_state_19 == False:
        print("Sensor_19")
    if sensor_state_11 == False:
        print("Sensor_11")
    if sensor_state_6 == False:
        print("Sensor_6")
    else:
        pass
        # print("No gas")
    # time.sleep(0.1)
