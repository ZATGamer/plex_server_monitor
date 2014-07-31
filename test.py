import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
red = GPIO.PWM(7, 50)

red.start(0)
while True:
        red.ChangeDutyCycle(50)

