from program import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/100Days')
def hundred_days():
    return render_template('100Days.html')

@app.route('/dummy')
def dummy():
    return "Dummy Route"

@app.route('/iso_queues')
def iso_queues():
    return render_template('iso_queues.html')