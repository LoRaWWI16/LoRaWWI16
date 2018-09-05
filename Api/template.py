import time, datetime
import ttn
import pymysql
import bottle
pymysql.install_as_MySQLdb()
from bottle import route,run,template,static_file
import bottle_mysql

app_id = "lorawwi16"
access_key = "ttn-account-v2.fD4fuJqNXvmZ3h8QXc8ExxG-CQDtJWeBKiURmVecz-4"

Lora = pymysql.connect(host="localhost",  # your host, usually localhost
                       user="Lora",  # your username
                       passwd="JfEpK54GTzjVqHbT",  # your password JfEpK54GTzjVqHbT
                       db="Lora")  # name of the data base


plugin = bottle_mysql.Plugin(dbuser = "Lora", dbpass = "JfEpK54GTzjVqHbT",dbname = "Lora")
app = bottle.Bottle()
app.install(plugin)


# you must create a Cursor object. It will let
#  you execute all the queries you need
cursor = Lora.cursor()


@app.route('/')
def index():
    print(printdb())
    handler = ttn.HandlerClient(app_id, access_key)

    # using mqtt client
    mqtt_client = handler.data()
    mqtt_client.set_uplink_callback(uplink_callback)

    mqtt_client.connect()
    time.sleep(60)
    mqtt_client.close()
    cursor.close()
    Lora.close()

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

    cursor.execute("select * from Daten")
    result = cursor.fetchall()
    return result

def uplink_callback(msg, client):
  print("Received uplink from ", msg.dev_id)


  add_daten = ("INSERT INTO Daten "
               "(Typ, Zeitstempel) "
               "VALUES (%s, %s)")

  if(msg.port == 1):
    data_msg = ('outputbasket', msg.payload_fields.outputbasket)
  if (msg.port == 2):
    data_msg = ('buzzer', msg.payload_fields.buzzer)
  if (msg.port == 3):
    data_msg = ('presencebutton', msg.payload_fields.presencebutton)
  if (msg.port == 4):
    data_msg = ('lightsensor', msg.payload_fields.lightsensor)
  if (msg.port == 5):
    data_msg = ('case', msg.payload_fields.case)


  # Insert new Data
  cursor.execute(add_daten, data_msg)
  emp_no = cursor.lastrowid

  # Make sure data is committed to the database
  Lora.commit()





