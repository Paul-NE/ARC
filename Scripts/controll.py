from threading import Thread
from IMU import IMU
from ups import INA219

imu = IMU(addr=0x68)
ups = INA219(addr=0x41)

