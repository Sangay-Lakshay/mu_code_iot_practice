from ptpma import PMAButton
from ptoled import PTOLEDDisplay
from ptpma import PMALed
from time import sleep

button1= PMAButton("D0")
button2=PMAButton("D4")
led1 = PMALed("D1")
led2 = PMALed("D2")
led3 = PMALed("D3")
oled_screen = PTOLEDDisplay()

def pressedb1():
    led3.on()
    oled_screen.draw_multiline_text("GO!")
    sleep(2)
    led3.off()
    led1.on()
    oled_screen.draw_multiline_text("WAIT!")
    sleep(1)
    led1.off()
    led2.on()
    oled_screen.draw_multiline_text("STOP!")
    sleep(5)
    led2.off()


def pressedb2():

    led2.on()
    oled_screen.draw_multiline_text("STOP!")
    sleep(2)
    led2.off()
    led1.on()
    oled_screen.draw_multiline_text("WAIT!")
    sleep(1)
    led1.off()
    led3.on()
    oled_screen.draw_multiline_text("GO!")
    sleep(5)
    led3.off()

button1.when_pressed = pressedb1
button2.when_released =pressedb2



