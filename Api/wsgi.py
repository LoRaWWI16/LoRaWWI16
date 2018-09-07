import time, datetime
import ttn
import pymysql
import bottle
from bottle import template


import os

os.chdir("/var/www/Lora/views")

app = bottle.Bottle()

app_id = "lorawwi16"
access_key = "ttn-account-v2.fD4fuJqNXvmZ3h8QXc8ExxG-CQDtJWeBKiURmVecz-4"

Lora = pymysql.connect(host="localhost",  # your host, usually localhost
                       user="Lora",  # your username
                       passwd="JfEpK54GTzjVqHbT",  # your password JfEpK54GTzjVqHbT
                       db="Lora")  # name of the data base







@app.route('/')
def index():

    row = printdb()
    last = row[-1]
    lastdate = last[0]
    count = len(row)
    first = row[0]
    now = datetime.datetime.now()
    dur = int((now - lastdate).total_seconds())
    if dur > 28800:
        test = True
    else:
        test = False
    if row:
        return template('index.tpl',row=row, last=last, count=count, first=first, test=test)

def printdb():

    cursor = Lora.cursor()
    cursor.execute("select * from Daten")
    result = cursor.fetchall()
    cursor.close()
    return result



application = app



