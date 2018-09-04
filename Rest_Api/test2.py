#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="Lora",         # your username
                     passwd="JfEpK54GTzjVqHbT",  # your password
                     db="Lora")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cursor = db.cursor()

# Use all the SQL you like
add_daten = ("INSERT INTO Daten "
               "(Typ, Zeitstempel) "
               "VALUES (%s, %s)")


data_msg = ('1','20181111111111')

# Insert new Data
cursor.execute(add_daten, data_msg)
emp_no = cursor.lastrowid

# Make sure data is committed to the database
db.commit()

cursor.close()
db.close()
