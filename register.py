from ptpma import PMAButton
import sqlite3 as sql
button = PMAButton("D5")


name=input("enter name")
cid= int(input("enter CID"))
dob=input("enter date of birth")
gender=input("gender")


def buttonpress():
    with sql.connect('practicalExam.sql') as con:
        cur=con.cursor()
        cur.execute("insert into register (name, CID, birthdate, gender) values(?,?,?,?)",(name, cid, dob, gender))
        cur.commit()

buttonpress = button.when_pressed