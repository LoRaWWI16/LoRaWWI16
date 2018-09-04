import bottle
import bottle_mysql

@route('/')
def index():
    return template('index', name = 'Julia')

if __name__ == '__main__':
    run(debug = True, reloader = True)
