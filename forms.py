from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class loginForm(FlaskForm):
    username = StringField ('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField ('Contraseña', validators=[DataRequired()])
    submit = SubmitField ('Enviar')