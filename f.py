from ptpma import PMAButton
from ptpma import PMALed
from ptoled import PTOLEDDisplay
from time import sleep
from ptpma import PMABuzzer

led1 = PMALed("D2")
led2 = PMALed("D3")
button = PMAButton("D1")
buzzer = PMABuzzer("D0")
s = PTOLEDDisplay()

def on_button_pressed():
    led1.on()
    buzzer.on()
    s.draw_multiline_text("On Your Mark!")
    sleep(0.3)
    led1.off()
    buzzer.off()
    s.draw_multiline_text("")
    sleep(1)

    led1.on()
    buzzer.on()
    s.draw_multiline_text("Get Set!")
    sleep(0.3)
    led1.off()
    buzzer.off()
    s.draw_multiline_text("")
    sleep(1)

    led2.on()
    buzzer.on()
    s.draw_multiline_text("Go!")
    sleep(1)
    led2.off()
    buzzer.off()
    s.draw_multiline_text("")

button.when_pressed = on_button_pressed