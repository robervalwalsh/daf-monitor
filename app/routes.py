from flask import render_template, redirect, flash, request
from app import app
from app.dryair.forms import DryAirForm

@app.route('/daf-monitor/')
@app.route('/daf-monitor/home')
def home():
    return render_template('home.html',title='Home')

@app.route('/daf-monitor/dryair/add-entry', methods=['GET', 'POST'])
def dryair():
    title = 'Dry Air'
    form = DryAirForm()
    if form.validate_on_submit():
        return redirect('/daf-monitor/home')
        
    if request.method == 'POST':
        if form.submit.data:
            return render_template('dryair_new.html',title=title, form=form)

    return render_template('dryair_add.html',title=title, form=form)

