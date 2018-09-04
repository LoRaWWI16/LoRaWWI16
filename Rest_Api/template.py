import bottle
import pymysql
pymysql.install_as_MySQLdb()
from bottle import route,run,template
import bottle_mysql

db = bottle_mysql.connect(host="159.69.91.59",  # your host, usually localhost
                       user="root",  # your username
                       passwd="16WIW20#",  # your password
                       db="Lora")  # name of the data base

@route('/')
def index():
    return template('index', name = 'Julia')

if __name__ == '__main__':
    run(debug = True, reloader = True)
