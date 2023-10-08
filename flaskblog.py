from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

# Remember to make this an environment key
app.config['SECRET_KEY'] = 'ff3c8fec043ae5f58ae6dd0c3b154dac'

posts = [
    {
        "author": "Joel Nyongesa",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "October 8 2023"
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "October 8 2023"
    },

]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been logged in!", 'success')
            return redirect(url_for('home'))
        else:
            flash('Log In Unsuccessful. Please check username and passord', 'danger')
    return render_template('login.html', title="Login", form=form)



if __name__ == "__main__":
    app.run(debug=True)