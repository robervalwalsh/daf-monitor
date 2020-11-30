from math import pi
from datetime import datetime

from flask import render_template, redirect, flash, request, url_for
from app import app
from app.dryair.forms import DryAirForm
from app.dryair.forms import DryAirForm25c
from app.dryair.forms import DryAirForm26
from app.dryair.forms import DryAirForm26_comp2

import pandas as pd


from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import DatetimeTickFormatter
from bokeh.models import Legend

@app.route('/daf-monitor/')
@app.route('/daf-monitor/home')
def home():
    return render_template('home.html',title='Home')

@app.route('/daf-monitor/dryair')
def dryair():
    title = 'Dry Air Compressor'
    fname = {}
    fname['25c'] = '/var/www/html/daf-monitor/compressor_data_25c.csv'
    fname['26']  = '/var/www/html/daf-monitor/compressor_data_26.csv'
#    fname['26_comp2']  = '/var/www/html/daf-monitor/compressor_data_26_comp2.csv'
    df = {}
    dates = {}
    values = {}
    
    hist_plots = ['dewpoint','system','dutycycle','avgflow']
    for bld in fname:
        df[bld] = pd.read_csv(fname[bld])
        dates[bld] = [ datetime.strptime(ds, "%Y-%m-%d %H:%M:%S") for ds in  df[bld]['date'].to_list()]
        values[bld] = {}
        timespan = [((d2-d1).seconds/60 + (d2-d1).days*24*60) for d1,d2 in zip(dates[bld], dates[bld][1:])]
        values[bld]['dewpoint'] = df[bld]['dewpoint'].to_list() 
        if bld == '26':
            values[bld]['system'] = df[bld]['compressor'].to_list() 
        else:
            values[bld]['system'] = df[bld]['system'].to_list() 
        system_duration = [(v2-v1)*60 for v1,v2 in zip(values[bld]['system'], values[bld]['system'][1:])]
        if bld == '26':
            volume = [ sd*393. for sd in system_duration ]
        else:
            pump1_duration = [(v2-v1)*60 for v1,v2 in zip(df[bld]['pump1'].to_list(), df[bld]['pump1'].to_list()[1:])]
            pump2_duration = [(v2-v1)*60 for v1,v2 in zip(df[bld]['pump2'].to_list(), df[bld]['pump2'].to_list()[1:])]
            volume = [(p1+p2)*883.33 for p1,p2 in zip(pump1_duration,pump2_duration)]
        avgflow = [ v/t for v,t in zip(volume, timespan)]
        avgflow.insert(0, 0)
        values[bld]['avgflow'] = avgflow
        dutycycle = [x/y for x, y in zip(system_duration, timespan)]
        dutycycle.insert(0, 0)
        values[bld]['dutycycle'] = dutycycle
            
            
            
    color = {}
    color['25c'] = 'navy'
    color['26'] = 'firebrick'
#    color['26_comp2'] = 'red'
    
#    hist_plots = ['dewpoint','system','dutycycle','avgflow']
    hist_plots_render = {}
    hist_plots_lable = {}
    hist_plots_lable['dewpoint'] = 'dew point (\xb0C)'
    hist_plots_lable['system'] = 'duration (h)'
    hist_plots_lable['dutycycle'] = 'duty cycle'
    hist_plots_lable['avgflow'] = 'average flow (l/min)'
    hist_plots_lable['compressor'] = 'compressor (h)'
    p = {}
    date_format = ['%d %b %Y']
    rc = {}
    rl = {}
    legend = {}
    for idx,h in enumerate(hist_plots):
        p[h] = figure(plot_width=700, plot_height=400,x_axis_type="datetime",toolbar_location='right')
        p[h].xaxis.formatter=DatetimeTickFormatter(
              microseconds=date_format,
              milliseconds=date_format,
              seconds=date_format,
              minsec=date_format,
              minutes=date_format,
              hourmin=date_format,
              hours=date_format,
              days=date_format,
              months=date_format,
              years=date_format
             )
        var = h
        rc[h] = {}
        rl[h] = {}
        items = []
        for bld in fname:
            legend_label = 'Building '+bld
            if h == 'system':
                if bld == '26':
                    var = 'compressor'
                legend_label += ' ('+var+')'
            rc[h][bld] = p[h].circle(dates[bld],values[bld][h], color=color[bld], legend_label=legend_label)
#            rl[h][bld] = p[h].line(dates[bld],values[bld][h], line_width=1, line_color=color[bld], legend=legend_label)
#            r[h][bld] = p[h].circle(dates[bld],values[bld][h], color=color[bld], legend_label=legend_label)
#            items.append((legend_label,[r[h][bld]]))
        p[h].xaxis.major_label_orientation = pi/8
        p[h].xaxis.axis_label = 'Local time'
        p[h].yaxis.axis_label = hist_plots_lable[h]
        p[h].legend.click_policy='hide'
        if idx != 0:
            p[h].legend.location='top_left'
#        legend[h] = Legend(items=items, location="center")
#        legend[h].click_policy="hide"
#        p[h].add_layout(legend[h], 'right')
    
        hist_plots_render[h] = {}
        hist_plots_render[h]['script'], hist_plots_render[h]['div'] = components(p[h])
    
    return render_template('dryair.html',title=title,hplots=hist_plots_render)


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

@app.route('/daf-monitor/dryair/add-data/25c', methods=['GET', 'POST'])
def dryair_add_25c():
    title = 'Dry Air'
    form = DryAirForm25c()
    if form.validate_on_submit():
#        return redirect('/daf-monitor/home')
        form.save_data()
        return render_template('dryair_new_25c.html',title=title, form=form)
        
    return render_template('dryair_add_25c.html',title=title, form=form)

@app.route('/daf-monitor/dryair/add-data/26', methods=['GET', 'POST'])
def dryair_add_26():
    title = 'Dry Air'
    form = DryAirForm26()
    if form.validate_on_submit():
#        return redirect('/daf-monitor/home')
        form.save_data()
        return render_template('dryair_new_26.html',title=title, form=form)
        
    return render_template('dryair_add_26.html',title=title, form=form)

@app.route('/daf-monitor/dryair/add-data/26_comp2', methods=['GET', 'POST'])
def dryair_add_26_comp2():
    title = 'Dry Air'
    form = DryAirForm26_comp2()
    if form.validate_on_submit():
#        return redirect('/daf-monitor/home')
        form.save_data()
        return render_template('dryair_new_26_comp2.html',title=title, form=form)
        
    return render_template('dryair_add_26_comp2.html',title=title, form=form)

