from flask import Flask, render_template, request
import sqlite3 as sql
from ptpma import PMAButton

button = PMAButton("D5")

app = Flask(__name__)
@app.route('/homepage')
def index():
    return render_template("homepage.html")


@app.route('/counterpage')
def index1():
    con=sql.connect('db.sql')
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute('select count(*), (select count(*) from user where gender ="M"), (select count(*) from user where gender ="F") from user')
    rows=cur.fetchall()
    return render_template("counter.html", rows=rows)

@app.route('/registration', methods=['GET', 'POST'])
def index2():
    if request.method == 'POST':
        name=request.form['name']
        cid=request.form['cid']
        dob=request.form['dob']
        gender=request.form['gen']

        with sql.connect('db.sql') as con:
            cur=con.cursor()
            cur.execute("insert into user (name, CID, birthdate, gender) values(?,?,?,?)",(name, cid, dob, gender))
            con.commit()

    return render_template("registration.html")
    con.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')