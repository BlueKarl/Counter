#coding:utf-8

from flask import Flask, request, render_template

from QPSmonitor.search import search

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('test.html')

@app.route('/request/data/<date_value>')
def count(date_value):
    data, numbers = search(date_value)
    return data

@app.route('/request/numbers/<date_value>')
def numbers(date_value):
    data, numbers = search(date_value)
    return numbers


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
