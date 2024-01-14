from ptpma import PMALightSensor
from time import sleep
import sqlite3 as sq
import matplotlib.pyplot as p
import numpy as np

light_sensor = PMALightSensor("A0")
reading="{}".format(light_sensor.reading)

with open("/home/pi/Desktop/iot.py/iot.txt",'a') as f:
    while True:
        f.write(reading)
f.close()


x = np.arange(0.0, 10.0, 0.1)
p.plot(x, np.sin(2*x), ‘g--’, label=‘sine’)
p.plot(x, np.cos(2*x), ‘r-’, label=‘cosine’)
p.legend() # or p.legend((‘sine’, ‘cosine’))
p.xlabel(‘X values’)
p.ylabel(‘Y values’)
p.title(‘Plot of Trig Functions’)
p.grid(True)
p.show()