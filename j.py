from ptpma import PMASoundSensor
from time import sleep

sound_sensor = PMASoundSensor("A0")

while True:
    # Returns reading the amount of sound in the room
    print(sound_sensor.reading)
    sleep(1)