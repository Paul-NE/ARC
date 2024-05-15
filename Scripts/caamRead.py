from picamera2 import Picamera2
import cv2
import IMU

cam = Picamera2()
config = cam.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)})
cam.configure(config)
cam.start()

fourcc = cv2.VideoWriter_fourcc(*'XVID') 
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
imu_file = open("imu.txt", 'w')
imu_sensor = IMU.IMU()

try:
    while True:
        frame = cam.capture_array()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = frame[::-1, ::-1]
        show_frame = cv2.resize(frame, (640, 480))
        out.write(frame)
        accelerometer_data, gyroscope_data, temperature = imu_sensor.read()
        imu_file.write(f"{accelerometer_data};{gyroscope_data};{temperature}\n")
        # cv2.imshow("Camera", show_frame)
        cv2.waitKey(1)
except KeyboardInterrupt:
    pass
finally:    
    imu_file.close()
    out.release()
