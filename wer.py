from ptpma import PMALightSensor, PMASoundSensor, PMAButton, PMALed, PMAUltrasonicSensor, PMABuzzer
from time import sleep, time


led = PMALed("D0")
buttonOff = PMAButton("D1")
buttonOn =PMAButton("D2")
buzzer = PMABuzzer("D3")
ultrasonic = PMAUltrasonicSensor("D4")
light = PMALightSensor("A0")
sound = PMASoundSensor("A1")

while True:
    print(light.reading)
    sleep(1)