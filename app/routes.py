from flask import render_template, redirect, flash, request, url_for
from app import app
from app.dryair.forms import DryAirForm



@app.route('/daf-monitor/')
@app.route('/daf-monitor/home')
def home():
    return render_template('home.html',title='Home')

@app.route('/daf-monitor/dryair')
def dryair():
    title = 'Dry Air Compressor'
    return render_template('dryair.html',title=title)


@app.route('/daf-monitor/dryair/add-data', methods=['GET', 'POST'])
def dryair_add():
    title = 'Dry Air'
    form = DryAirForm()
    if form.validate_on_submit():
#        return redirect('/daf-monitor/home')
        form.save_data()
        return render_template('dryair_new.html',title=title, form=form)
        
#    if request.method == 'POST':
#        if form.submit.data:
#            return "<h1> OI OI </h1>"
#            return render_template('dryair_new.html',title=title, form=form)
            
    return render_template('dryair_add.html',title=title, form=form)

