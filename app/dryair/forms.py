from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, BooleanField, SubmitField, TimeField, DateTimeField, SelectField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea
from datetime import datetime

class DryAirForm(FlaskForm):
    location = SelectField('Location', default=0, choices=[(0, "Select one location"), (1, "Building 25c"), (2, "Building 26")], validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    date = DateTimeField('Date and time', default=datetime.today, validators=[DataRequired()])
    dewpoint = DecimalField('Dew point (\xb0C)', validators=[DataRequired()])
    runtime = DecimalField('Runtime total (hours)', validators=[DataRequired()])
    runtime1 = DecimalField('Runtime unit 1 (hours)', validators=[DataRequired()])
    runtime2 = DecimalField('Runtime unit 2 (hours)', validators=[DataRequired()])
    message = StringField('Message (optional)', widget=TextArea())
    submit = SubmitField('Add entry')
    clear = SubmitField('Clear')
