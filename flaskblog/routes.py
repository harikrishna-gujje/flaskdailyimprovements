from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm


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
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('registration.html', title='Registration', form = form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'Login successful for {form.email.data}!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login failed for {form.email.data}!', 'danger')
    return render_template('login.html', title='sign in', form=form)
