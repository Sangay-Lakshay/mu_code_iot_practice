from ptpma import PMAButton
from ptoled import PTOLEDDisplay
from ptpma import PMALed
from time import sleep

button = PMAButton("D0")
led1 = PMALed("D1")
led2 = PMALed("D2")
led3 = PMALed("D3")
oled_screen = PTOLEDDisplay()

def press():
    led1.on()


def release():
    led1.off()
    led2.on()
    led2.off()

button.when_pressed = press
button.when_released = release