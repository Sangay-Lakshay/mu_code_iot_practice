from flask import Flask, render_template, request
import sqlite3 as sql


app = Flask(__name__)
@app.route('/home')
def index():
    return render_template("charo.html")


@app.route('/showFriends')
def index1():
    con=sql.connect('charo.sql')
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute('select * from friend')
    rows=cur.fetchall()
    return render_template("friend.html", rows=rows)

@app.route('/addFriends', methods=['GET', 'POST'])
def index2():

    if request.method == 'POST':
        name=request.form['name']
        gender=request.form['gen']
        contact=request.form['contact']
        address=request.form['address']

        with sql.connect('charo.sql') as con:
            cur=con.cursor()
            cur.execute('insert into friend(Name, gender, contact, address) values(?,?,?,?)',(name, gender,contact, address))
            cur.commit()

    return render_template("addfriend.html")
    con.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')