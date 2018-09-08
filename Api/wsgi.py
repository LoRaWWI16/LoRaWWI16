import datetime
import pymysql
import bottle
from bottle import route,template,static_file, BaseTemplate
#import value as value
#BaseTemplate.defaults['symbol_name'] = value
import os

os.chdir("/var/www/Lora")

Lora = pymysql.connect(host="localhost",  # your host, usually localhost
                       user="Lora",  # your username
                       passwd="JfEpK54GTzjVqHbT",  # your password JfEpK54GTzjVqHbT
                       db="Lora")  # name of the data base


app = bottle.default_app()
BaseTemplate.defaults['get_url'] = app.get_url

# Static Routes
@route('static/<filename:path>', name='static')
def server_static(filename):
    return static_file(filename, root='static')

@app.route('/')
def index():
    row = printdb()
    last = row[-1]
    lastdate = last[0]
    count = len(row)
    first = row[0]
    now = datetime.datetime.now()
    dur = int((now - lastdate).total_seconds())
    hours = int(dur/3600)
    days = int(hours/24)
    chart = server_static('chart.png')
    if row:
        return template('index.tpl',row=row, last=last, count=count, first=first, dur=dur, hours=hours, days=days, chart=chart)


def printdb():

    cursor = Lora.cursor()
    cursor.execute("select * from Daten")
    result = cursor.fetchall()
    cursor.close()
    return result



application = app



