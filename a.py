from ptpma import PMAButton
from ptoled import PTOLEDDisplay
from ptpma import PMALed
from time import sleep

button1 = PMAButton("D0")
button2 =PMAButton("D4")
led1 = PMALed("D1")
led2 = PMALed("D2")
led3 = PMALed("D3")
oled_screen = PTOLEDDisplay()

def pressbutton1():
    led1.on()
    led2.on()
    led3.on()

def pressbutton2():
    led1.off()
    led2.off()
    led3.off()

button1.when_pressed=pressbutton1
button2.when_released=pressbutton2
