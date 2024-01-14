from pitop.pma import Potentiometer, LED
from time import sleep

potentiometer = Potentiometer("A0")
red = LED("D1")
yellow = LED("D0")
green = LED("D2")

while True:
    print(potentiometer.position)
    sleep(0.1)
    if  potentiometer.position >334 and potentiometer.position < 666:
        red.on ()
        yellow.off()
        green.off()
    elif potentiometer.position<333:
        red.off()
        yellow.on()
        green.off()
    elif potentiometer.position >667:
        red.off()
        yellow.off()
        green.on()