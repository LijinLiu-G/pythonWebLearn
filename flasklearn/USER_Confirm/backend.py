from flask import Flask, render_template, redirect, url_for,request
from flask_login import LoginManager, login_required, login_user, logout_user, UserMixin, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin):
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return f'<User {self.id}>'


users = [
    User(1),
    User(2),
    User(3)
]


@login_manager.user_loader
def load_user(user_id):
    return next((user for user in users if user.id == int(user_id)), None)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        user_id = int(request.form['user_id'])
        # user_id = request.form['user_id']
        user = next((user for user in users if user.id == user_id), None)
        if user:
            login_user(user)
            return redirect(url_for('dashboard'))
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', current_user=current_user)


if __name__ == '__main__':
    app.run(debug=True)