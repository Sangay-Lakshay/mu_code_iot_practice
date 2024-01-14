from ptpma import PMASoundSensor
from time import sleep
from ptpma import PMAButton
from ptpma import PMALed
from ptpma import PMABuzzer
from ptoled import PTOLEDDisplay

buzzer = PMABuzzer("D0")
button=PMAButton("D1")
led1=PMALed("D2")
led2=PMALed("D3")
s = PTOLEDDisplay()
sound=PMASoundSensor("A0")

while True:
    if sound.reading>170:
        led1.on()
    else:
        led1.off()