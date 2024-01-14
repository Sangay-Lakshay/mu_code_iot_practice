import pyttsx3
from pitop.keyboard import KeyboardButton
from ptoled import PTOLEDDisplay
from time import sleep
from pitop.pma import LED, Buzzer

red_led = LED("D1")
yellow_led = LED("D0")
green_led = LED("D2")
buzzer = Buzzer("D3")
s = PTOLEDDisplay()

engine = pyttsx3.init()
voices = engine.getProperty('voices')


r = KeyboardButton("r")
y = KeyboardButton("y")
g = KeyboardButton("g")
b = KeyboardButton("b")

def red_on():
    red_led.on()
    s.draw_multiline_text("RED ON")
    engine.say('RED ON')

def red_off():
    red_led.off()
    s.draw_multiline_text("RED OFF")
    engine.say('RED OFF')


def yellow_on():
    yellow_led.on()
    s.draw_multiline_text("YELLOW ON")
    engine.say('YELLOW ON')
    engine.runAndWait()

def yellow_off():
    yellow_led.off()
    s.draw_multiline_text("YELLOW OFF")
    engine.say('YELLOW OFF')


def green_on():
    green_led.on()
    s.draw_multiline_text("GREEN ON")
    engine.say('GREEN ON')

def green_off():
    green_led.off()
    s.draw_multiline_text("GREEN OFF")
    engine.say('GREEN OFF')
def buzzer_on():
    buzzer.on()
    s.draw_multiline_text ("BUZZ")

def buzzer_off():
    buzzer.off()
    s.draw_multiline_text ("NO BUZZ")

r.when_pressed = red_on
r.when_released = red_off
y.when_pressed = yellow_on
y.when_released = yellow_off
g.when_pressed = green_on
g.when_released = green_off
b.when_pressed = buzzer_on
b.when_released = buzzer_off