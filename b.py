import pyttsx3
from ptpma import PMAButton
from ptpma import PMALed
from ptpma import PMAUltrasonicSensor
from ptpma import PMABuzzer
from ptoled import PTOLEDDisplay
from time import sleep

button = PMAButton("D0")
led1 = PMALed("D1")
led2 = PMALed("D2")
s = PTOLEDDisplay()
buzzer = PMABuzzer("D4")
dis = PMAUltrasonicSensor("D5")

engine = pyttsx3.init()
voices = engine.getProperty('voices')


def on_button_pressed():
    while True:
        if dis.distance <= 20 and dis.distance>10:
            buzzer.off()

            s.draw_multiline_text("ALMOST THERE!")
            engine.say('Almost there')
            engine.runAndWait()
            sleep(0.3)
            buzzer.off()
            sleep(0.3)
            led1.on()
            led2.off()
        elif dis.distance<=30 and dis.distance>20:
            buzzer.off()
            s.draw_multiline_text("OK GO!")
            engine.say('Ok Go backward')
            engine.runAndWait()
            sleep(0.5)
            buzzer.off()
            sleep(0.5)
            led1.on()
            led2.off()

        elif dis.distance<=10:
            s.draw_multiline_text("STOP!")
            engine.say('Stop!')
            engine.runAndWait()
            buzzer.off()
            led1.on()


        else:
            buzzer.off()
            led2.off()
            led1.off()


button.when_pressed=on_button_pressed