import datetime
import pymysql
import bottle
import value as value

from bottle import route,run,template,static_file, BaseTemplate
#BaseTemplate.defaults['symbol_name'] = value


app_id = "lorawwi16"
access_key = "ttn-account-v2.fD4fuJqNXvmZ3h8QXc8ExxG-CQDtJWeBKiURmVecz-4"

Lora = pymysql.connect(host="localhost",  # your host, usually localhost
                       user="root",  # your username
                       passwd="",  # your password JfEpK54GTzjVqHbT
                       db="Lora")  # name of the data base



# you must create a Cursor object. It will let
#  you execute all the queries you need
cursor = Lora.cursor()
app = bottle.default_app()
BaseTemplate.defaults['get_url'] = app.get_url

# Static Routes
@route('/static/<filename:path>', name='static')
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

    cursor.execute("select * from Daten")
    result = cursor.fetchall()
    return result


if __name__ == '__main__':
    run(debug=True,reloader=True,app=app)




