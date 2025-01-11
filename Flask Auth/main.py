from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3


app = Flask(__name__)
app.secret_key = 'sdgiojksafgij'

@app.route('/')
def home():
    if 'user' not in session:
        return render_template("index.html")
    else:
        return redirect("/secrets")


@app.route('/register')
def register():
    if 'user' not in session:
        return render_template("register.html")
    else:
        return redirect("/secrets")

@app.route("/add_user", methods=['POST'])
def add_user():
    form = request.form
    password = form['password']
    hash = generate_password_hash(password, method='pbkdf2', salt_length=8)
    conn = sqlite3.connect('./instance/users.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(f"INSERT INTO user (email, password, name) VALUES ('{form['email']}', '{hash}', '{form['name']}')")
    conn.commit()
    conn.close()
    return redirect("/login")

@app.route('/login', methods=['GET'])
def login():
    if 'user' not in session:
        error = None
        arguments = request.args
        try:
            if arguments['error'] == "unauthorized":
                error = 'Incorrect username or password.'
        except:
            pass
        finally:
            return render_template('login.html', error=error)
    else:
        return redirect("/secrets")

@app.route("/validate", methods=['POST'])
def validate():
    form = request.form
    conn = sqlite3.connect('./instance/users.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM user")
    values = cur.fetchall()
    users = [dict(value) for value in values]
    conn.close()
    for user in users:
        if user['email'] == form['email']:
            if check_password_hash(user['password'], form['password']):
                session['user'] = user['name']
                return redirect('/secrets')
    return redirect('/login?error=unauthorized')

@app.route('/secrets')
def secrets():
    if 'user' in session:
        return render_template("secrets.html", username=session['user'])
    return redirect('/')


@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop("user", None)
        return redirect("/")
    else:
        return redirect('/')


@app.route('/download')
def download():
    return send_from_directory(directory='./static/files', path='./cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
