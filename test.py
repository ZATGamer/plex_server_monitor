import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)

p = GPIO.PWM(7, 50)

p.start(0)
while True:
    for 1 in range(100):
        p.ChangeDutyCycle(1)
        sleep(0.02)
    for 1 in range(100):
        p.ChangeDutyCycle(100-1)
        sleep(0.02)
