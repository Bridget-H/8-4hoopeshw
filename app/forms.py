from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo,


class RegisterForm(FlaskForm):
    posts = StringField('post', validators=[DataRequired()])
    submit = SubmitField()