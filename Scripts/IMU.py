import mpu6050
import time
from threading import Thread


class IMU:
    def __init__(self, addr=0x68) -> None:
        self.sensor = mpu6050.mpu6050(addr)
        self.accelerometer_data = self.sensor.get_accel_data()
        self.gyroscope_data = self.sensor.get_gyro_data()
        self.temperature = self.sensor.get_temp()
    def read(self):
        self.accelerometer_data = self.sensor.get_accel_data()
        self.gyroscope_data = self.sensor.get_gyro_data()
        self.temperature = self.sensor.get_temp()
        return self.accelerometer_data, self.gyroscope_data, self.temperature
    
if __name__=="__main__":
    while True:
        imu = IMU(0x68)
        accelerometer_data, gyroscope_data, temperature = imu.read()

        print("Accelerometer data:", accelerometer_data)
        print("Gyroscope data:", gyroscope_data)
        print("Temp:", temperature)

        # Wait for 1 second
        time.sleep(1)   