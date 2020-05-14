from flask import render_template
from app import app
from app.dryair.forms import DryAirForm

@app.route('/daf-monitor/')
@app.route('/daf-monitor/home')
def home():
    return render_template('home.html',title='Home')

@app.route('/daf-monitor/dryair/add')
def dryair():
    title = 'Dry Air'
    form = DryAirForm()
    locations = ['25c','26']
    return render_template('dryair.html',title=title, locations=locations, form=form)
