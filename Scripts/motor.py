from gpiozero import Motor
from time import sleep
motor1 = Motor(5, 22)
print(motor1)
motor1.forward(1)
sleep(5)
motor1.stop()
