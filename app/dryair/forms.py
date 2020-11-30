import os.path

from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, BooleanField, SubmitField, TimeField, DateTimeField, SelectField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea
from datetime import datetime
import pandas as pd

class DryAirForm(FlaskForm):
    submit = SubmitField('  Submit Form  ')
    # building 25
    date_25c = DateTimeField('Date', default=datetime.today, validators=[DataRequired()])
    dewpoint_25c = DecimalField('Dew point (\xb0C)', validators=[DataRequired()])
    system_25c = DecimalField('System (hours)', validators=[DataRequired()])
    pump1_25c = DecimalField('Pump 1 (hours)', validators=[DataRequired()])
    pump2_25c = DecimalField('Pump 2 (hours)', validators=[DataRequired()])
    # building 26
    date_26 = DateTimeField('Date', default=datetime.today, validators=[DataRequired()])
    dewpoint_26 = DecimalField('Dew point (\xb0C)', validators=[DataRequired()])
    compressor_26 = DecimalField('Compressor (hours)', validators=[DataRequired()])
    # building 26_comp2
    date_26_comp2 = DateTimeField('Date', default=datetime.today, validators=[DataRequired()])
    dewpoint_26_comp2 = DecimalField('Dew point (\xb0C)', validators=[DataRequired()])
    pump1_26_comp2 = DecimalField('Pump 1 (hours)', validators=[DataRequired()])
    pump2_26_comp2 = DecimalField('Pump 2 (hours)', validators=[DataRequired()])
    
    def save_data(self):
        # Building 25c
        data25c = { 'date': [self.date_25c.data.strftime('%Y-%m-%d %H:%M:%S')],
                    'system': [str(self.system_25c.data)],
                    'pump1': [str(self.pump1_25c.data)],
                    'pump2': [str(self.pump2_25c.data)],
                    'dewpoint': [str(self.dewpoint_25c.data)] }
        df_25c =  pd.DataFrame(data=data25c)
        
        fname25c = '/var/www/html/daf-monitor/compressor_data_25c.csv' 
        if os.path.isfile(fname25c):
            df_25c.to_csv(fname25c, mode='a', index=False, header=False)
        else:
            df_25c.to_csv(fname25c, mode='a', index=False, header=True)
            
        # Building 26
        data26 = { 'date': [self.date_26.data.strftime('%Y-%m-%d %H:%M:%S')],
                   'compressor': [str(self.compressor_26.data)],
                   'dewpoint': [str(self.dewpoint_26.data)] }
        df_26 =  pd.DataFrame(data=data26)
        
        fname26 = '/var/www/html/daf-monitor/compressor_data_26.csv' 
        if os.path.isfile(fname26):
            df_26.to_csv(fname26, mode='a', index=False, header=False)
        else:
            df_26.to_csv(fname26, mode='a', index=False, header=True)
            
        # Building 26_comp2
        data26_comp2 = { 'date': [self.date_26_comp2.data.strftime('%Y-%m-%d %H:%M:%S')],
                    'pump1': [str(self.pump1_26_comp2.data)],
                    'pump2': [str(self.pump2_26_comp2.data)],
                    'dewpoint': [str(self.dewpoint_26_comp2.data)] }
        df_26_comp2 =  pd.DataFrame(data=data26_comp2)
        
        fname26_comp2 = '/var/www/html/daf-monitor/compressor_data_26_comp2.csv' 
        if os.path.isfile(fname26_comp2):
            df_26_comp2.to_csv(fname26_comp2, mode='a', index=False, header=False)
        else:
            df_26_comp2.to_csv(fname26_comp2, mode='a', index=False, header=True)
            
            
