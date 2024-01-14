from pitop.pma import Potentiometer
from time import sleep,time
import matplotlib.pyplot as plt
import numpy as np
potentiometer = Potentiometer("A0")

x_data = []
y_data = []
start_time = time()
while True:
    p=potentiometer.position
    elapsed_time = time() - start_time
    x_data.append(elapsed_time)
    y_data.append(p)

    x_data = x_data[-10:]
    y_data = y_data[-10:]

    plt.plot(x_data, y_data)
    plt.draw()
    plt.pause(0.2)
    plt.title('Potentiometer')
    plt.ylabel('potentiometer position')
    plt.xlabel('Time (seconds)')