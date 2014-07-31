from gpiocrust import PWMOutputPin, OutputPin, Header
from time import sleep

while True:
    with Header() as header:
        PWMOutputPin(11,50.0,value=1.0)
        sleep(5)
