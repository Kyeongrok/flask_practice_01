from flask import Flask, render_template, flash, redirect, url_for
from forms import RegistrationForm, LoginForm
from os import environ
import glob, csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '48494dc3dfa160ba017699929a90ecc1'
posts = [
    {
        'author':'Corey Schafer',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'April 20, 2018'
    },
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 20, 2018'
    }
]
@app.route('/')
def home():
    # 해당 위치에 파일이 있는지
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    # 해당 위치에 파일이 있는지
    return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('about.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
