from ptpma import PMAButton
from ptpma import PMAUltrasonicSensor
from ptpma import PMALed
from ptpma import PMABuzzer
from time import sleep


ledR=PMALed("D0")
ledG=PMALed("D1")
ledY=PMALed("D2")
buzzer = PMABuzzer("D4")
dis = PMAUltrasonicSensor("D3")

while True:
    print(dis.distance)
    if dis.distance<=30:
        buzzer.on()
        ledG.off()
        ledR.on()
        ledY.off()
    elif dis.distance<=50 and dis.distance>30:
        buzzer.off()
        ledG.off()
        ledR.off()
        ledY.on()
    elif dis.distance>50:
        buzzer.off()
        ledG.on()
        ledR.off()
        ledY.off()
    else:
        buzzer.off()
        ledG.off()
        ledR.off()
        ledY.off()







