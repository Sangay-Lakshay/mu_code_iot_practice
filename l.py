import pyttsx3
from ptpma import PMAButton
from ptoled import PTOLEDDisplay
from ptpma import PMALed
from ptpma import PMALightSensor
from time import sleep

button = PMAButton("D4")
led1 = PMALed("D1")
led2 = PMALed("D2")
s = PTOLEDDisplay()
light_sensor = PMALightSensor("A0")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("rate",100)
engine.setProperty('voices', "russian")

def button_on():
    while True:
        if light_sensor.reading > 200:
            led1.on()
            led2.off()
            s.draw_multiline_text("AHH MY EYE!")
            engine.say('AHH MY EYE')
            engine.runAndWait()
            sleep(0.3)

        elif light_sensor.reading <100 and light_sensor.reading>10:
            led1.off()
            led2.on()
            s.draw_multiline_text("Thank God!")
            engine.say('Thank God')
            engine.runAndWait()
            sleep(0.3)

        elif light_sensor.reading <10:
            led1.off()
            led2.off()
            s.draw_multiline_text("TOO DARK!")
            engine.say('TOO DARK')
            engine.runAndWait()
            sleep(0.3)

button.when_pressed =button_on