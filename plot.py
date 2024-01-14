from flask import Flask
import matplotlib.pyplot as plt
import numpy as np
from flask import Response

app = Flask(__name__)

@app.route('/plot')
def plot():
    x_data = [1,2,3,4,5,6]
    y_data = [5,10,15,20,25,30]
    plt.plot(x_data,y_data)
    plt.title('Plot')
    plt.ylabel('position')
    plt.xlabel('Time (seconds)')
    plt.savefig('/static/images/new_plot.png')
    return render_template('untitled1.html', name = 'new_plot', url ="/static/images/new_plot.png")

if __name__ == '__main__':
   app.run(debug = True)