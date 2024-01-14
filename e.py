import pyttsx3
from ptpma import PMAButton
from ptoled import PTOLEDDisplay
from ptpma import PMALed
from ptpma import PMALightSensor
from time import sleep

button = PMAButton("D0")
led1 = PMALed("D1")
led2 = PMALed("D2")
s = PTOLEDDisplay()
light_sensor = PMALightSensor("A0")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("rate",100)

def button_on():
    while True:
        light_sensor.reading > 200:
            led1.on()
            s.draw_multiline_text("AHH MY EYE!")
            engine.say('AHH MY EYE')
            engine.runAndWait()
            sleep(0.3)

