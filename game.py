import pyttsx3
from ptpma import PMALed
from ptpma import PMABuzzer, PMAButton
from ptoled import PTOLEDDisplay
from time import sleep
from pitop.keyboard import KeyboardButton
import sqlite3 as sq
import random

red_led = PMALed("D1")
yellow_led = PMALed("D0")
green_led = PMALed("D2")
buzzer = PMABuzzer("D3")
s = PTOLEDDisplay()
b = PMAButton("D4")

engine = pyttsx3.init()
voices = engine.getProperty('voices')

alp1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def key():
    if a == alp1[ran]:
        engine.say("Correct")
        engine.runAndWait()
    else:
        engine.say("Incorrect")
        engine.runAndWait()
while True:
    ran = random.randrange(0,26)
    engine.say(alp1[ran])
    a = KeyboardButton(alp1[ran])
    engine.runAndWait()
    a.when_pressed = key

    sleep(4)

