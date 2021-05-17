from flask import render_template, flash, redirect, url_for, request

from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, CreateTableForm
from flaskblog.model import User, Post
from flaskblog.domain.dynamo_table import Table
import boto3
import ast, json
from libs.DecimalEncoder import DecimalEncoder


dynamodb = boto3.resource('dynamodb')

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
    # return render_template('home.html', posts=posts)
    return redirect(url_for('auction_list'))


@app.route('/about')
def about():
    # 해당 위치에 파일이 있는지
    return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(password=form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

@app.route('/table_list')
def table_list():
    tables = Table('auction2').list_table()
    # for table in tables['TableNames']:
    #     print(type(table))
    return render_template('table_list.html', title='Table List', list=tables['TableNames'])


@app.route('/auction_list', methods=['GET', 'POST'])
def auction_list():
    t = Table('auction2')
    r = t.select_by_pk('20210514')
    l = []
    for i in r['Items']:
        d = ast.literal_eval((json.dumps(i, cls=DecimalEncoder)))
        l.append(d['data1'])
    total = len(l)
    print(l[0])
    return render_template('auction_list.html', total=total, title='Auction List', list=l)


@app.route('/create_table', methods=['GET', 'POST'])
def create_table():
    form = CreateTableForm()
    if form.validate_on_submit():
        table_name = form.table_name.data

        check_whether_the_table_has_been_exsist = None
        Table().create_table(table_name)


    return render_template('create_table.html', title='Create Table', form=form)

