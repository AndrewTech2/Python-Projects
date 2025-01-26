from flask import Flask, session, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap5
import datetime, sqlite3
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = '141413412432141242141242'
bootstrap = Bootstrap5(app)

@app.route('/', methods=['POST', 'GET'])
def index():
    if 'name' in session:
        today = datetime.datetime.today()
        today_date = today.strftime("%Y-%m-%d")
        time_now = today.strftime('%H:%M')
        if request.method == 'POST':
            form = request.form
            conn = sqlite3.connect('data/messages.db')
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute(f"INSERT INTO messages (USER, CONTENT, DATE, TIME) VALUES (?, ?, ?, ?)", [session['name'], form['content'], today_date, time_now])
            conn.commit()
            conn.close()
            return redirect("/")
        conn = sqlite3.connect('data/messages.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM messages WHERE DATE = '{today_date}'")
        values = cur.fetchall()
        messages = [dict(value) for value in values]
        conn.close()
        messages = messages[::-1]
        return render_template("chat.html", messages=messages, year=str(datetime.datetime.today().year))
    else:
        return render_template('index.html', year=str(datetime.datetime.today().year))

@app.route("/signup", methods=['POST', 'GET'])
def sign_up():
    if 'name' in session:
        return redirect('/')
    if request.method == 'POST':
        form = request.form
        name = form['username']
        password = form['password']
        conn = sqlite3.connect('data/users.sql')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute('SELECT * FROM users')
        values = cur.fetchall()
        users = [dict(value) for value in values]
        print(users)
        # Check if user in database. If yes, then check the password.
        for user in users:
            if user['name'] == name:
                if check_password_hash(user['password'], password):
                    session['name'] = name
                    return redirect("/")
                else:
                    return 'Passwords do not match!'
        # The next runs if user is not logged in.
        hash = generate_password_hash(password, method='pbkdf2')
        cur.execute(f"INSERT INTO users (name, password) VALUES ('{name}', '{hash}')")
        conn.commit()
        conn.close()
        session['name'] = name
        return redirect("/")
    return render_template('signup.html', year=str(str(datetime.datetime.today().year)))

@app.route("/logout")
def logout():
    if 'name' in session:
        session.pop("name")
    return redirect('/')

app.run(debug=True)