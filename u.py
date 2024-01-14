import thingspeak
from ptpma import PMAUltrasonicSensor
from time import sleep
channel = 1375137
write = "TR5OH5DP5H1BX48K"
read = "HU2XSXCKP9SUP0RX"


def measure(channel):
    a = PMAUltrasonicSensor("D4")
    print (a.distance)
    response = channel.update({"field1":a.distance})

c = thingspeak.Channel(channel, write, read)
while True:
    measure(c)
    sleep(15)