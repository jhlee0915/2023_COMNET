from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    UserId = StringField('Id', validators=[DataRequired()])
    UserPassword = StringField('Password', validators=[DataRequired()])
