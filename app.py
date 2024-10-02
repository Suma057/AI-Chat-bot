from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = 'your_secret_key'
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# Sample user data (can be expanded later)
users = {'testuser': {'id': 1, 'username': 'testuser', 'password': bcrypt.generate_password_hash('password').decode('utf-8')}}

class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

@login_manager.user_loader
def load_user(user_id):
    for user in users.values():
        if user['id'] == int(user_id):
            return User(user['id'], user['username'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and bcrypt.check_password_hash(user['password'], password):
            login_user(User(user['id'], username))
            return redirect(url_for('chat'))
        flash('Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/chat', methods=['GET', 'POST'])
@login_required
def chat():
    answer = None
    if request.method == 'POST':
        query = request.form['query']
        from chatbot import generate_answer
        document_text = "Loaded document text here"  # Placeholder for document text
        answer = generate_answer(query, document_text)
    return render_template('chat.html', answer=answer)

if __name__ == '__main__':
    app.run(debug=True)

