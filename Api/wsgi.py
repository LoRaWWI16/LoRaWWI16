import time, datetime
import ttn
import pymysql
import bottle
from bottle import template


app = bottle.Bottle()




@app.route('/')
def index():

    return "Hello"
@app.route('/test')
def hell():
    return template('test.tpl')


application = app
