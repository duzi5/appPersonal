from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired




class formulario_login(FlaskForm):
    usuario = StringField('usuario', validators = [DataRequired()])
    senha = StringField('senha', validators = [DataRequired()])
    lembrar = BooleanField('lembrar')
    
