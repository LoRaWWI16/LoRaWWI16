import time, datetime
import ttn
import pymysql
import bottle
from bottle import route, template, run, debug, request, static_file, TEMPLATE_PATH

app = bottle.Bottle()

app_id = "lorawwi16"
access_key = "ttn-account-v2.fD4fuJqNXvmZ3h8QXc8ExxG-CQDtJWeBKiURmVecz-4"

Lora = pymysql.connect(host="localhost",  # your host, usually localhost
                       user="root",  # your username
                       passwd="",  # your password JfEpK54GTzjVqHbT
                       db="Lora")  # name of the data base
# you must create a Cursor object. It will let
#  you execute all the queries you need
cursor = Lora.cursor()


def uplink_callback(msg, client):
  cursor = Lora.cursor()

  print(msg)


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
  cursor.close()


handler = ttn.HandlerClient(app_id, access_key)

#using mqtt client
mqtt_client = handler.data()
mqtt_client.set_uplink_callback(uplink_callback)

mqtt_client.connect()
time.sleep(61)
mqtt_client.close()




