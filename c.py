from ptpma import PMABuzzer
from ptpma import PMAButton
from ptpma import PMALed
from time import sleep

led1 = PMALed("D2")
led2 = PMALed("D3")
button = PMAButton("D1")
buzzer = PMABuzzer("D0")


def on_button_pressed():
    led2.off()
    while True:
        led1.on()
        buzzer.on()
        sleep(0.3)
        led1.off()
        buzzer.off()
        sleep(0.3)


def on_button_released():
    led1.off()
    led2.on()
    buzzer.off()




button.when_pressed = on_button_pressed
button.when_released = on_button_released
