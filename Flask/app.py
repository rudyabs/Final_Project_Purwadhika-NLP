from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm 

app = Flask(__name__)

# membuat secret key (generate secret key dengan cmd: python -> import secrets -> secrets.token_hex(16))
app.config['SECRET_KEY'] = '79ad1ee3d585c0bfda62c676a95a8c66'

# dummy post data
posts = [
    {
        'author':'Rudy',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'July 20, 2019'
    },
    {
        'author':'Aunallah',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date_posted':'July 21, 2019'
    }
]



@app.route('/')
@app.route('/home')
def home():
   return render_template('home.html', posts=posts)

@app.route('/about')
def about():
   return render_template('about.html', title='About')

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): # validasi saat submit
        flash(f'Akun dari {form.username.data} berhasil dibuat!!!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@test.com' and form.password.data == 'password':
            flash('Berhasil Log In Gan!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Gagal Gan. Coba cek lagi email dan passwordnya', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
