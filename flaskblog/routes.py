from flask import render_template, url_for, flash, redirect
from flaskblog import app, db, bcrypt
from flaskblog.models import User
from flaskblog.forms import RegistrationForm, LoginForm
from flask_login import login_user, logout_user, login_required



posts = [
    {
        'author' : 'harikrishna',
        'title': 'post1',
        'content': 'first post description',
        'date_posted':'22nd of july 2021'
    },
    {
        'author' : 'corey',
        'title': 'post2',
        'content': 'second post description',
        'date_posted':'23nd of july 2021'
    }
]


@app.route('/')
@app.route("/home")
def home():
    return render_template('home.html', posts=posts, title='Title')


@app.route("/about")
def about():
    return render_template('about.html', title='about me')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        print(hashed_password)
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('registration.html', title='Registration', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            flash(f'Login successful for {form.email.data}!', 'info')
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash(f'Login unsuccessful, Please check email and password.', 'danger')
    return render_template('login.html', title='sign in', form=form)


@app.route("/logout", methods=['GET', 'POST'])
def logout():
    logout_user()
    return render_template('home.html', posts=posts, title='Title')


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='My Account')