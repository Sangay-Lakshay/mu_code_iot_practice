from ptpma import PMALightSensor
from ptpma import PMASoundSensor
from ptoled import PTOLEDDisplay
from time import sleep, time
import matplotlib.pyplot as plt
import numpy as np

light_sensor = PMALightSensor("A0")
sound_sensor = PMASoundSensor("A1")
mini_screen = PTOLEDDisplay()
mini_screen.set_max_fps(1)
canvas = mini_screen.canvas
canvas.set_font_size(15)
# this lines creates the figure for plotting
plt.ion()
fig = plt.figure()

# these lines create empty lists to hold data
x_data = []
y_data = []

a_data = []

# this line sets the starting time
start_time = time()

# code inside a while True loop runs over and over
# this loop reads from the sensor and plots the data
while True:
    # this line reads from light sensor
    light_level = (light_sensor.reading)
    sound_level = (sound_sensor.reading)
    # this line calculates how much time has passed since starting
    elapsed_time = time() - start_time

    # these lines add data to the x and y lists
    x_data.append(elapsed_time)
    y_data.append(light_level)
    a_data.append(sound_level)

    # these lines limit x and y lists to 20 items
    x_data = x_data[-10:]
    y_data = y_data[-10:]
    a_data = a_data[-10:]

    plt.subplot(211)
    plt.plot(x_data, y_data)
    plt.draw()
    plt.pause(0.1)
    plt.title('Light Sensor input over Time')
    plt.ylabel('Light Level')
    plt.xlabel('Time (seconds)')


    canvas.clear()
    canvas.multiline_text(canvas.top_left(), 'light level: ' + str(light_level))
    canvas.line((0, 40, light_level / 4, 40), width = 10)
    mini_screen.draw()
    sleep(1)

    plt.subplot(212)
    plt.plot(x_data, a_data)
    plt.draw()
    plt.pause(0.1)
    # these lines format the graph
    plt.title('Sound Sensor input over Time')
    plt.ylabel('Sound Level')
    plt.xlabel('Time (seconds)')
