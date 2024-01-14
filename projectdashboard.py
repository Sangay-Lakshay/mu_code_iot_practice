from flask import Flask, render_template, request, redirect, session, flash
from ptpma import PMALightSensor, PMASoundSensor, PMAButton, PMALed, PMAUltrasonicSensor, PMABuzzer
from time import sleep, time
import thingspeak
import sqlite3 as sql

channel = 1413147
write = "V43CJVV116OL3N5J"
read = "4V3SD6GIKMTGE66K"

led1 = PMALed("D0")
led2 = PMALed("D5")
buttonOff = PMAButton("D1")
buttonOn =PMAButton("D2")
buzzer = PMABuzzer("D3")
ultrasonic = PMAUltrasonicSensor("D4")
light = PMALightSensor("A0")
sound = PMASoundSensor("A1")

def measure(channel, a, b, c):
    response = channel.update({"field1":a, "field2":b, "field3":c})

chann = thingspeak.Channel(channel, write, read)

def pressbuttonOn():
    led1.on()
    led2.on()

def pressbuttonOff():
    led1.off()
    led2.off()

def alarm():
    for i in range(30):
        buzzer.on()
        sleep(0.1)
        buzzer.off()
        sleep(0.1)

buttonOff.when_pressed=pressbuttonOff
buttonOn.when_pressed=pressbuttonOn

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'
@app.route('/homepageon')
def indexon():
    username = session['user']
    c = sql.connect('project.sql')
    with c:
        cur = c.cursor()
        cur.execute("create table if not exists user (username varchar(50), email varchar(50), address varchar(50), password varchar(30))")
        cur.execute("create table if not exists alarm (ultrasonic int, light int, sound int, flag int, date text, username varchar(50), foreign key (username) references user(username))")
        while True:
            measure(chann, ultrasonic.distance, sound.reading, light.reading)

            if ultrasonic.distance < 10:
                cur.execute("insert into alarm (ultrasonic, light, sound, flag, date, username) values (?,NULL, NULL, 1, CURRENT_TIMESTAMP, ?)", (ultrasonic.distance, username))
                c.commit()
                alarm()
                break
            elif sound.reading > 190:
                cur.execute("insert into alarm (ultrasonic, light, sound, flag, date, username) values (NULL, NULL, ?, 1, CURRENT_TIMESTAMP, ?)", (sound.reading, username) )
                c.commit()
                alarm()
                break
            elif light.reading > 50:
                cur.execute("insert into alarm (ultrasonic, light, sound, flag, date, username) values (NULL, ?, NULL, 1, CURRENT_TIMESTAMP, ?)", (light.reading, username) )
                c.commit()
                alarm()
                break
    c.close()


    con = sql.connect("project.sql")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select ultrasonic, STRFTIME('%H:%M, %d/%m/%Y', date) as date from alarm where ultrasonic is not NULL and username = ? order by date desc limit 3 ", [username])
    Frows = cur.fetchall();

    cur.execute("select sound, STRFTIME('%H:%M, %d/%m/%Y', date) as date from alarm where sound is not NULL and username = ? order by date desc limit 3 ", [username])
    Srows = cur.fetchall();

    cur.execute("select light, STRFTIME('%H:%M, %d/%m/%Y', date) as date from alarm where light is not NULL and username = ? order by date desc limit 3 ", [username])
    Trows = cur.fetchall();

    return render_template("indexon.html", Frows=Frows, Srows=Srows, Trows=Trows, username=username)

@app.route('/homepageoff')
def indexoff():
    username = session['user']

    con = sql.connect("project.sql")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select ultrasonic, STRFTIME('%H:%M, %d/%m/%Y', date) as date from alarm where ultrasonic is not NULL and username = ? order by date desc limit 3 ", [username])
    Frows = cur.fetchall();

    cur.execute("select sound, STRFTIME('%H:%M, %d/%m/%Y', date) as date from alarm where sound is not NULL and username = ? order by date desc limit 3 ", [username])
    Srows = cur.fetchall();

    cur.execute("select light, STRFTIME('%H:%M, %d/%m/%Y', date) as date from alarm where light is not NULL and username = ? order by date desc limit 3 ", [username])
    Trows = cur.fetchall();

    return render_template("indexoff.html", Frows=Frows, Srows=Srows, Trows=Trows, username=username)

@app.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template("register.html")

    elif request.method == 'POST':
        con = sql.connect("project.sql")
        user_name = request.form['user_name']
        address = request.form['address']
        email = request.form['email']
        password = request.form['password']
        password_repeat = request.form['password_repeat']

        if (password == password_repeat):

            with con:
                cur = con.cursor()
                cur.execute("create table if not exists user (username varchar(50), email varchar(50), address varchar(50), password varchar(30))")
                cur.execute("create table if not exists alarm (ultrasonic int, light int, sound int, flag int, date text, username varchar(50), foreign key (username) references user(username))")
                cur.execute("INSERT INTO user (username,email,address,password) VALUES (?,?,?,?)",(user_name,email,address,password) )
                con.commit()
                flash("Record successfully added")
                return redirect('/')
        else:
            con.rollback()
            flash("error in insert operation")
        con.close()

@app.route('/', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        con = sql.connect("project.sql")
        user_name = request.form['user_name']
        password = request.form['password']

        with con:
            cur = con.cursor()
            cur.execute("create table if not exists user (username varchar(50), email varchar(50), address varchar(50), password varchar(30))")
            cur.execute("create table if not exists alarm (ultrasonic int, light int, sound int, flag int, date text, username varchar(50), foreign key (username) references user(username))")
            cur.execute("select password from user where username = ?", [user_name] )
            con.commit()
            row = cur.fetchone()
            if (password == row[0]):
                session['user'] = user_name
                return redirect('/homepageoff', )
    else:
        con.rollback()
        flash("error in insert operation")
    con.close()

@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')