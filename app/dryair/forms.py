import os.path

from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, BooleanField, SubmitField, TimeField, DateTimeField, SelectField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea
from datetime import datetime
import pandas as pd
import getpass

# https://influxdb-client.readthedocs.io/en/stable/index.html
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import pytz

def get_username():
    return getpass.getuser()

def write_db(point):
    ### influxdb API token dry-air-test: scaIB2eqP5d3LpC4bI1bSxhCUlm4z3ObsdsH48nxshOnRSrkIF8GDdljXlonkcRsHfCKRJwF1ddY5Xx44QHKCw==
    # InfluxDB configuration
    db_token = 'EMvjVW7gow2-MWa7Ly3T6duu_F3qQ9yki5MuPZuqQrM-bl6sewhxpxmH5Ob0cptpKoxn-4qIP6ifD7XlJ4B9dg=='
    db_bucket = 'dry-air'
    if get_username() != 'cleangat':
        db_token = 'scaIB2eqP5d3LpC4bI1bSxhCUlm4z3ObsdsH48nxshOnRSrkIF8GDdljXlonkcRsHfCKRJwF1ddY5Xx44QHKCw=='
        db_bucket = 'dry-air-test'
    db_url = 'http://influx2.131.169.217.81.nip.io'
    db_org = 'desy'
    db_client = InfluxDBClient(url=db_url, token=db_token, org=db_org)
    db_write_api = db_client.write_api(write_options=SYNCHRONOUS)
    db_write_api.write(bucket=db_bucket, org=db_org, record=point)

### TO DO: Manyimporvements to do, e.g. use one function and pass building/compressor name as parameter to the function

            
class DryAirForm25c(FlaskForm):
    submit = SubmitField('  Submit Form  ')
    # building 25
    date_25c = DateTimeField('Date', default=datetime.today, validators=[DataRequired()])
    dewpoint_25c = DecimalField('Dew point (\xb0C)', validators=[DataRequired()])
    system_25c = DecimalField('System (hours)', validators=[DataRequired()])
    pump1_25c = DecimalField('Pump 1 (hours)', validators=[DataRequired()])
    pump2_25c = DecimalField('Pump 2 (hours)', validators=[DataRequired()])
    username = get_username()
    
    def save_data(self):
        # Building 25c
        data25c = { 'date': [self.date_25c.data.strftime('%Y-%m-%d %H:%M:%S')],
                    'system': [str(self.system_25c.data)],
                    'pump1': [str(self.pump1_25c.data)],
                    'pump2': [str(self.pump2_25c.data)],
                    'dewpoint': [str(self.dewpoint_25c.data)] }
        df_25c =  pd.DataFrame(data=data25c)
        
        fname25c = f'/home/{self.username}/daf-monitoring/data/dryair/compressor_data_25c.csv' 
        if os.path.isfile(fname25c):
            df_25c.to_csv(fname25c, mode='a', index=False, header=False)
        else:
            df_25c.to_csv(fname25c, mode='a', index=False, header=True)
        # DB point
        # Convert local Berlin time to UTC and then to Unix timestamp (seconds)
        berlin = pytz.timezone('Europe/Berlin')
        local_dt = berlin.localize(self.date_25c.data)
        utc_dt = local_dt.astimezone(pytz.utc)
        unix_timestamp = int(utc_dt.timestamp())
        db_structure = {
            "measurement": "compressor",
            "tags": {"unit": "25C"},
            "fields": { "dewpoint_degC": float(self.dewpoint_25c.data),
                        "system_hours": float(self.system_25c.data),
                        "pump1_hours": float(self.pump1_25c.data),
                        "pump2_hours": float(self.pump2_25c.data)
                      },
            "time": unix_timestamp
        }
        point = Point.from_dict(db_structure, WritePrecision.S)
        write_db(point)
          
class DryAirForm26(FlaskForm): 
    submit = SubmitField('  Submit Form  ')
    # building 26
    date_26 = DateTimeField('Date', default=datetime.today, validators=[DataRequired()])
    dewpoint_26 = DecimalField('Dew point (\xb0C)', validators=[DataRequired()])
    compressor_26 = DecimalField('Compressor (hours)', validators=[DataRequired()])
    username = get_username()
    
    def save_data(self):
        # Building 26
        data26 = { 'date': [self.date_26.data.strftime('%Y-%m-%d %H:%M:%S')],
                   'compressor': [str(self.compressor_26.data)],
                   'dewpoint': [str(self.dewpoint_26.data)] }
        df_26 =  pd.DataFrame(data=data26)
        
        fname26 = f'/home/{self.username}/daf-monitoring/data/dryair/compressor_data_26.csv' 
        if os.path.isfile(fname26):
            df_26.to_csv(fname26, mode='a', index=False, header=False)
        else:
            df_26.to_csv(fname26, mode='a', index=False, header=True)
        # DB point
        # Convert local Berlin time to UTC and then to Unix timestamp (seconds)
        berlin = pytz.timezone('Europe/Berlin')
        local_dt = berlin.localize(self.date_26.data)
        utc_dt = local_dt.astimezone(pytz.utc)
        unix_timestamp = int(utc_dt.timestamp())
        db_structure = {
            "measurement": "compressor",
            "tags": {"unit": "26-1"},
            "fields": { "dewpoint_degC": float(self.dewpoint_26.data),
                        "compressor_hours": float(self.compressor_26.data)
                      },
            "time": unix_timestamp
        }
        point = Point.from_dict(db_structure, WritePrecision.S)
        write_db(point)            
            
class DryAirForm26_comp2(FlaskForm):
    submit = SubmitField('  Submit Form  ')
    # building 26_comp2
    date_26_comp2 = DateTimeField('Date', default=datetime.today, validators=[DataRequired()])
    dewpoint_26_comp2 = DecimalField('Dew point (\xb0C)', validators=[DataRequired()])
    pump1_26_comp2 = DecimalField('Pump 1 (hours)', validators=[DataRequired()])
    pump2_26_comp2 = DecimalField('Pump 2 (hours)', validators=[DataRequired()])
    volume_26_comp2 = DecimalField('Volume (m\xb3)', validators=[DataRequired()])
    username = get_username()
    
    def save_data(self):
        # Building 26_comp2
        data26_comp2 = { 'date': [self.date_26_comp2.data.strftime('%Y-%m-%d %H:%M:%S')],
                    'pump1': [str(self.pump1_26_comp2.data)],
                    'pump2': [str(self.pump2_26_comp2.data)],
                    'dewpoint': [str(self.dewpoint_26_comp2.data)], 
                    'volume': [str(self.volume_26_comp2.data)] }
        df_26_comp2 =  pd.DataFrame(data=data26_comp2)
        
        fname26_comp2 = f'/home/{self.username}/daf-monitoring/data/dryair/compressor_data_26_comp2.csv' 
        if os.path.isfile(fname26_comp2):
            df_26_comp2.to_csv(fname26_comp2, mode='a', index=False, header=False)
        else:
            df_26_comp2.to_csv(fname26_comp2, mode='a', index=False, header=True)
        # DB point
        # Convert local Berlin time to UTC and then to Unix timestamp (seconds)
        berlin = pytz.timezone('Europe/Berlin')
        local_dt = berlin.localize(self.date_26_comp2.data)
        utc_dt = local_dt.astimezone(pytz.utc)
        unix_timestamp = int(utc_dt.timestamp())
        db_structure = {
            "measurement": "compressor",
            "tags": {"unit": "26-2"},
            "fields": { "dewpoint_degC": float(self.dewpoint_26_comp2.data),
                        "pump1_hours": float(self.pump1_26_comp2.data),
                        "pump2_hours": float(self.pump2_26_comp2.data),
                        "volume_m3": float(self.volume_26_comp2.data)
                      },
            "time": unix_timestamp
        }
        point = Point.from_dict(db_structure, WritePrecision.S)
        write_db(point)  
            
