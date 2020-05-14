from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, BooleanField, SubmitField, TimeField, DateTimeField, SelectField
from wtforms.validators import DataRequired

class DryAirForm(FlaskForm):
    location = SelectField('Location', choices=[(0, "Building 25c"), (1, "Building 26")], validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    dewpoint = DecimalField('Dew point', validators=[DataRequired()])
#    var1 = DecimalField('Var1', validators=[DataRequired()])
#    var2 = DecimalField('Var1', validators=[DataRequired()])
#    var3 = DecimalField('Var1', validators=[DataRequired()])
    date = DateTimeField('Date and time', format='%d.%m.%Y %H:%M:%S', validators=[DataRequired()])
    runtime = DecimalField('Runtime total (???)', validators=[DataRequired()])
    runtime1 = DecimalField('Runtime unit 1', validators=[DataRequired()])
    runtime2 = DecimalField('Runtime unit 2', validators=[DataRequired()])
    submit = SubmitField('Submit')
