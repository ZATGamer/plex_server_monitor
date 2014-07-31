import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

red = GPIO.PWM(11, 50)
green = GPIO.PWM(13, 50)
blue = GPIO.PWM(15, 50)
red.start(0)
while True:
    red.ChangeDutyCycle(50)
    green.ChangeDutyCycle(50)
    blue.ChangeDutyCycle(50)
