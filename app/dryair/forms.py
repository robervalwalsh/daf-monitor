from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, BooleanField, SubmitField, TimeField
from wtforms.validators import DataRequired

class DryAirForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    temperature = DecimalField('Temperature', validators=[DataRequired()])
    var1 = DecimalField('Var1', validators=[DataRequired()])
    var2 = DecimalField('Var1', validators=[DataRequired()])
    var3 = DecimalField('Var1', validators=[DataRequired()])
    time_read = TimeField('Reading Time', validators=[DataRequired()])
    submit = SubmitField('Submit')
