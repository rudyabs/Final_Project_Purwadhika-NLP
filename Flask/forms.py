from flask_wtf import FlaskForm

from wtforms import StringField # untuk username akan ber-isi file tipe 'str'
from wtforms import PasswordField # untuk password
from wtforms import SubmitField # untuk mensubmit data
from wtforms import BooleanField # field berisi boolean (true/false)


from wtforms.validators import DataRequired # validators untuk data harus terisi
from wtforms.validators import Length # validators untuk panjang min/max karakter
from wtforms.validators import Email # validators apakah emailnya valid
from wtforms.validators import EqualTo # cek jika password dan confirm password sama

# buat form untuk register/Sign Up
class RegistrationForm(FlaskForm):
    # validators digunakan untuk cek apakah sudah sesuai dengan argument
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Passsword', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

# buat form untuk login/Sign In
class LoginForm(FlaskForm):
    
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')