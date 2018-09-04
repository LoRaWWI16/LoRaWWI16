from flask import Flask, request, render_template
from flask_restful import Api
from flask_mysqldb import MySQL
import requests
import pymysql




app = Flask(__name__)
api = Api(app)

@app.route('/')
def someName():

    db = pymysql.connect("159.69.91.59", "root", "16WIW20#", "Lora")
    cursor = db.cursor()
    SQLALCHEMY_POOL_RECYCLE = 90

    sql = "SELECT * from Lora"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('index.html', results=results)
    cursor.close()
    db.close()


if __name__ == '__main__':
    app.run(debug=True)