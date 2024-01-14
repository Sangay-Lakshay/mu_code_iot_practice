from ptpma import PMALightSensor
from time import sleep
import sqlite3 as sq
light_sensor = PMALightSensor("A0")

cur=sq.connect("/home/pi/sensor")
conn=cur.cursor()
while True:
    reading=light_sensor.reading
    conn.execute("insert into lightsensor(sensorvalue, time) values({},strftime('%s', 'now'))".format(reading))
    cur.commit()
    conn.execute("select serialNo, sensorvalue, datetime(time, 'unixepoch') from lightsensor")
    data=conn.fetchall()
    for i in data:
        print(i)
    sleep(3)