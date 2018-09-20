import datetime
import pymysql
import bottle
from bottle import route,template,static_file, BaseTemplate
import os
import plotly.plotly as py
import plotly.graph_objs as go
import plotly


os.chdir("/var/www/Lora")

def show_piechart(labels, values):
    py.sign_in("LoRaWAN", "FaALCNaPzblRxtH7dN1T")

    trace = go.Pie(labels=labels,
                   values=values,
                   textfont=dict(size=20),
                   marker={'colors': ['rgb(36, 187, 156)',
                                      'rgb(42, 63, 84)',
                                      'rgb(54, 153, 221)',
                                      'rgb(175, 49, 35)',
                                      'rgb(36, 73, 147)'],
                            'line': dict(color='#ffffff', width=5)},
                   hole=0.4)
    py.image.save_as([trace], filename='/var/www/Lora/static/donut.png')

def show_histo(x,y):
    py.sign_in("LoRaWAN", "FaALCNaPzblRxtH7dN1T")

    data = [go.Scatter(
        x=x,
        y=y)]

    layout = go.Layout(xaxis=dict(
        range=[x[0],
               x[-1]]
    ))

    fig = go.Figure(data=data, layout=layout)
    py.image.save_as(fig, '/var/www/Lora/static/histo.png')

Lora = pymysql.connect(host="localhost",  # your host, usually localhost
                       user="Lora",  # your username
                       passwd="JfEpK54GTzjVqHbT",  # your password JfEpK54GTzjVqHbT
                       db="Lora")  # name of the data base


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
    dutydate = fetch_last_dutydate()[-1][0]
    durdate = int((now-dutydate).total_seconds())
    dutydateh = int(durdate/3600)
    fillupdate = fetch_last_fillupdate()[-1][0]
    durupdate = int((now-fillupdate).total_seconds())
    fillupdateh = int(durupdate/3600)
    if lastdate > now-datetime.timedelta(hours=1):
        [labels, values] = fetch_chart_data()
        show_piechart(labels, values)
        [x,y]=fetch_histo_data()
        show_histo(x,y)
    if row:
        return template('index.tpl',row=row, last=last, count=count, first=first, dur=dur, hours=hours, days=days,
                        dutydate=dutydate, durdate=durdate, dutydateh=dutydateh, durupdate=durupdate, fillupdateh=fillupdateh)

def printdb():
    cursor = Lora.cursor()
    cursor.execute("select * from Daten")
    result = cursor.fetchall()
    cursor.close()
    return result

def fetch_chart_data():
    cursor = Lora.cursor()
    cursor.execute("select distinct Typ, count(Typ) from Daten group by Typ")
    data = cursor.fetchall()
    labels = []
    values = []
    for i in data:
        labels.append(i[0])
        values.append(i[1])
    cursor.close()
    return labels, values

def fetch_last_dutydate():
    cursor = Lora.cursor()
    cursor.execute("select max(Zeitstempel) from Daten where Typ='buzzer' group by Typ")
    data = cursor.fetchall()
    cursor.close()
    return data

def fetch_last_fillupdate():
    cursor = Lora.cursor()
    cursor.execute("select max(Zeitstempel) from Daten where Typ='case' group by Typ")
    data = cursor.fetchall()
    cursor.close()
    return data

def fetch_histo_data():
    cursor = Lora.cursor()
    cursor.execute("select Zeitstempel from Daten")
    data = cursor.fetchall()
    x = []
    y = []
    temp = []
    for i in data:
        temp.append(i[0].strftime('%x'))
    i = 0
    j = 1
    while i < len(temp):
        counter = 1
        while (temp[i] == temp[j]):
            j = j+1
            counter = counter + 1
            if j >= len(temp):
                j = j-1
                break

        x.append(temp[i])
        y.append(counter)
        i = j
        j = j + 1
        if i >= len(temp)-1:
            break
    cursor.close()
    print(x,y)
    return x,y


application = app



