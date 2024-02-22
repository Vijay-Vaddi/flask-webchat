from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class MessageForm(FlaskForm):

    username = StringField('Username')
    message = StringField('Message')
    send = SubmitField('Send')
    