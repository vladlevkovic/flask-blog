from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, validators


class PostForm(FlaskForm):
    title = StringField('Title', validators=[validators.DataRequired()])
    body = TextAreaField('Body', validators=[validators.DataRequired()])
    submit = SubmitField('Submit')
