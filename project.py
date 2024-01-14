from ptpma import PMALightSensor, PMASoundSensor, PMAButton, PMALed, PMAUltrasonicSensor, PMABuzzer
from time import sleep, time
import matplotlib.pyplot as plt
import numpy as np
import thingspeak
import sqlite3 as sql


channel = 1409137
write = "3IMQL8ZE9NVNHCQA"
read = "OTXJO8SNBIAHG4RK"

led = PMALed("D0")
buttonOff = PMAButton("D1")
buttonOn =PMAButton("D2")
buzzer = PMABuzzer("D3")
ultrasonic = PMAUltrasonicSensor("D4")
proButtonOff = PMAButton("D5")
proButtonOn =PMAButton("D6")
light = PMALightSensor("A0")
sound = PMASoundSensor("A1")

def measure(channel, a, b, c):
    response = channel.update({"field1":a, "field2":b, "field3":c})

chann = thingspeak.Channel(channel, write, read)

def pressbuttonOn():
    led.on()

def pressbuttonOff():
    led.off()

#def pressproButtonOff():



def alarm():
    for i in range(30):
        buzzer.on()
        sleep(0.1)
        buzzer.off()
        sleep(0.1)

def pressproButtonOn():
    c = sql.connect('project.sql')
    with c:
        cur = c.cursor()
        cur.execute("create table if not exists user (username varchar(50), email varchar(50), address varchar(50), password varchar(30))")
        cur.execute("create table if not exists alarm (ultrasonic int, light int, sound int,switch int, flag int, date text)")
        while True:
            ultrasonicReading = ultrasonic.distance
            soundReading = sound.reading
            lightReading = light.reading

            #measure(chann, ultrasonicReading, soundReading, lightReading)

            if ultrasonicReading <= 10:
                cur.execute("insert into alarm (ultrasonic, light, sound, switch, flag, date) values (1,NULL, NULL, NULL, 1, CURRENT_TIMESTAMP)")
                print(cur.lastrowid)
                c.commit()
                alarm()
            elif soundReading >= 120:
                cur.execute("insert into alarm (ultrasonic, light, sound, switch, flag, date) values (NULL, NULL, 1, NULL, 1, CURRENT_TIMESTAMP)" )
                c.commit()
                alarm()
            elif lightReading >= 50:
                cur.execute("insert into alarm (ultrasonic, light, sound, switch, flag, date) values (NULL, 1, NULL, NULL, 1, CURRENT_TIMESTAMP)" )
                c.commit()
                alarm()
            elif buttonOn.when_pressed == True:
                cur.execute("insert into alarm (ultrasonic, light, sound, switch, flag, date) values (NULL, NULL, NULL, 1, 1, CURRENT_TIMESTAMP)")
                c.commit()
                alarm()
    c.close()


buttonOff.when_pressed=pressbuttonOff
buttonOn.when_pressed=pressbuttonOn
#proButtonOff.when_pressed=pressproButtonOff
proButtonOn.when_pressed=pressproButtonOn