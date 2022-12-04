from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '4736823462990396067dc3e604073207'

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
def home():
    return render_template('home.html', posts=posts)

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    print('hello before')
    if form.validate_on_submit():
        print('hello')
        flash(f'Account Created for {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Registration', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/about")
def about():
    return render_template('about.html', title='About Us')


if __name__ == "__main__":
    app.run(debug=True)