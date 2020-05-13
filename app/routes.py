from flask import render_template
from app import app

@app.route('/daf-monitor/')
@app.route('/daf-monitor/home')
def home():
    return render_template('home.html',title='Home')

@app.route('/daf-monitor/dryair')
def dryair():
    title = 'Dry Air'
    return render_template('dryair.html',title=title)
