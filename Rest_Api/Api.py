import time
import ttn
import pymysql
import bottle
pymysql.install_as_MySQLdb()
from bottle import route,run,template
import bottle_mysql

app_id = "lorawwi16"
access_key = "ttn-account-v2.fD4fuJqNXvmZ3h8QXc8ExxG-CQDtJWeBKiURmVecz-4"

Lora = pymysql.connect(host="localhost",  # your host, usually localhost
                       user="root",  # your username
                       passwd="",  # your password JfEpK54GTzjVqHbT
                       db="Lora")  # name of the data base

plugin = bottle_mysql.Plugin(dbuser = "root", dbpass = "",dbname = "Lora")
app = bottle.Bottle()
app.install(plugin)


# you must create a Cursor object. It will let
#  you execute all the queries you need
cursor = Lora.cursor()


@app.route('/')
def index():
    #row = printdb()
    #for resault in row:
     #   print (resault[0])
    #if row:
        return template('index.tpl')

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


if __name__ == '__main__':
    run(app, host='localhost', port=8080)

    handler = ttn.HandlerClient(app_id, access_key)

    # using mqtt client
    mqtt_client = handler.data()
    mqtt_client.set_uplink_callback(uplink_callback)


    printdb()
    mqtt_client.connect()
    time.sleep(60)
    mqtt_client.close()
    cursor.close()
    Lora.close()


