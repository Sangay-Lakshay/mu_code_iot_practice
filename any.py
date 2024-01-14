from flask import Flask, render_template, request, flash
import matplotlib.pyplot as plt
from forms import ContactForm

app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form = form)
        else:
            return render_template('success.html')
    elif request.method == 'GET':
        return render_template('contact.html', form = form)

@app.route('/plot')
def plot():
    x_data = [1,2,3,4,5,6]
    y_data = [5,10,15,20,25,30]
    plt.plot(x_data,y_data)
    plt.title('Plot')
    plt.ylabel('position')
    plt.xlabel('Time (seconds)')
    plt.savefig('static/new_plot.png')
    return render_template('Untitled1.html', name = 'new_plot', url ='static/new_plot.png')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')