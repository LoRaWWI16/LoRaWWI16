from bottle import run, route, template
import plotly.plotly as py
import plotly.graph_objs as go

def show_piechart():
    py.sign_in("mal_l", "hW3FjktvEXFwW9Jzv2dy")

    labels = ['LED','Summer','Ausgabekorb','Ding','Bums']
    values = [23,35,43,25,34]
    trace = go.Pie(labels=labels, values=values)

    py.image.save_as([trace], filename='chart.png')
    return 'chart.png'

def show_histo():
    py.sign_in("mal_l", "hW3FjktvEXFwW9Jzv2dy")


