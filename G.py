from ptpma import PMAButton
from ptpma import PMAUltrasonicSensor
from ptpma import PMALed
from ptpma import PMABuzzer
from time import sleep
from ptoled import PTOLEDDisplay

buzzer = PMABuzzer("D0")
dis = PMAUltrasonicSensor("D4")
button=PMAButton("D1")
led1=PMALed("D2")
led2=PMALed("D3")
s = PTOLEDDisplay()

def on_button_pressed():
    while True:
        if dis.distance <= 20 and dis.distance>10:
            buzzer.on()

            s.draw_multiline_text("ALMOST THERE!")
            sleep(0.3)
            buzzer.off()
            sleep(0.3)
            led1.on()
            led2.off()
        elif dis.distance<=30 and dis.distance>20:
            buzzer.on()
            s.draw_multiline_text("OK GO!")
            sleep(0.5)
            buzzer.off()
            sleep(0.5)
            led1.on()
            led2.off()

        elif dis.distance<=10:
            s.draw_multiline_text("STOP!")
            buzzer.on()
            led1.on()


        else:
            buzzer.off()
            led2.off()
            led1.off()


def on_button_released():
    buzzer.off()
    led1.off()
    led2.off()

button.when_pressed=on_button_pressed
button.when_released=on_button_released