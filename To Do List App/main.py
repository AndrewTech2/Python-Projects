from tkinter.ttk import Label

from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, session, redirect, request
import sqlite3, random

from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = str(random.randint(10000000, 999999999))

@app.route("/", methods=['GET'])
def index():
    if 'name' not in session:
        try:
            error = request.args['error']
        except:
            error = False
        return render_template('signup.html', error=error)
    else:
        conn = sqlite3.connect('users.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM tasks WHERE email = '{session['name']}'")
        values = cur.fetchall()
        tasks = [dict(value) for value in values][::-1]
        return render_template('list.html', tasks=tasks, length=len(tasks))

@app.route("/login", methods=['GET'])
def login():
    if 'name' in session:
        return redirect('/')
    else:
        try:
            error = request.args['error']
        except:
            error = False
        return render_template('login.html', error=error)

@app.route("/check_user", methods=['POST'])
def check_user():
    form = request.form

    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    try:
        cur.execute(f"SELECT * FROM users WHERE email='{form['email']}'")
    except:
        return redirect("/login?error=incorrect")
    values = cur.fetchall()
    conn.close()
    user = [dict(value) for value in values]

    if check_password_hash(user[0]['password'], form['password']):
        session['name'] = user[0]['email']
        return redirect('/')
    else:
        return redirect("/login?error=incorrect")

@app.route("/create-account", methods=['POST'])
def create_account():
    form = request.form

    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    values = cur.fetchall()
    conn.close()
    users = [dict(value) for value in values]

    for user in users:
        if user['email'] == form['email']:
            return redirect("/?error=already_exists")

    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(f"INSERT INTO users VALUES ('{form['email']}', '{generate_password_hash(form['password'])}')")
    conn.commit()
    conn.close()

    return redirect("/login")

@app.route("/addtask", methods=['POST'])
def add_task():
    form = request.form
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM tasks WHERE email = '{session['name']}' and task = '{form['task']}'")
    values = cur.fetchall()
    if len(values) != 0:
        return redirect('/')
    cur.execute(f"INSERT INTO tasks (task, email, completed) VALUES ('{form['task']}', '{session['name']}', 'false')")
    conn.commit()
    conn.close()
    return redirect('/')

@app.route("/delete/<pid>")
def delete(pid):
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(f"DELETE FROM tasks WHERE task = '{pid}' AND email = '{session['name']}'")
    conn.commit()
    conn.close()
    return redirect('/')

@app.route("/completetask/<pid>")
def complete(pid):
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(f"UPDATE tasks SET completed = 'true' WHERE task = '{pid}' AND email = '{session['name']}'")
    conn.commit()
    conn.close()
    return redirect('/')

@app.route("/uncompletetask/<pid>")
def uncomplete(pid):
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(f"UPDATE tasks SET completed = 'false' WHERE task = '{pid}' AND email = '{session['name']}'")
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/logout")
def logout():
    session.pop('name')
    return redirect('/')

app.run(debug=True)