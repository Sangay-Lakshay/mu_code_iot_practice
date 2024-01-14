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

def button1press():
    led1.on()
    led2.on()
    led3.on()
    oled_screen.draw_multiline_text("Yolo!")

def button2press():
    led1.off()
    sleep(1)
    led2.off()
    sleep(1)
    led3.off()
    oled_screen.draw_multiline_text("BYE!")

button1.when_pressed=button1press
button2.when_released=button2press