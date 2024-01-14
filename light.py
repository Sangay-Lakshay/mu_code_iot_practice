from ptpma import PMALightSensor, PMASoundSensor, PMAButton, PMALed, PMAUltrasonicSensor, PMABuzzer
from time import sleep, time

light = PMALightSensor("A0")

while True:
    print(light.reading)
    sleep(1)
