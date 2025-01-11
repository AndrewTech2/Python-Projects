from flask import Flask, render_template, redirect, url_for, request, session
from flask_bootstrap import Bootstrap5
from flask_gravatar import Gravatar
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
from flask_ckeditor import CKEditor
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
ckeditor = CKEditor(app)
Bootstrap5(app)
gravatar = Gravatar(app)
app.secret_key = os.environ.get('secret_key')

@app.route("/register", methods=['GET'])
def register():
    error = False
    try:
        error = request.args['error']
    except:
        pass
    return render_template('register.html', error=error)

@app.route("/add_user", methods=['POST'])
def add_user():
    form = request.form

    password = generate_password_hash(password=form['password'], method='pbkdf2')

    conn = sqlite3.connect('./instance/posts.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('SELECT username FROM users')
    values = cur.fetchall()
    users = [dict(value) for value in values]
    conn.close()

    for user in users:
        if user['username'] == form['username']:
            return redirect("/register?error=already_exists")

    conn = sqlite3.connect('./instance/posts.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(f"INSERT INTO users (username, email, password) VALUES ('{form['username']}', '{form['email']}', '{password}')")
    conn.commit()
    conn.close()

    return redirect("/login")

@app.route("/login", methods=['GET'])
def login():
    error = False
    try:
        error = request.args['error']
    except:
        pass
    return render_template('login.html', error=error)

@app.route("/check_user", methods=['POST'])
def check_user():
    form = request.form
    conn = sqlite3.connect('./instance/posts.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    try:
        cur.execute(f"SELECT * FROM users WHERE username = '{form['username']}'")
    except:
        return redirect("/login?error=invalid")
    values = cur.fetchall()
    user = [dict(value) for value in values]
    conn.close()
    if check_password_hash(user[0]['password'], form['password']):
        session['name'] = user[0]['username']
        return redirect("/")
    else:
        return redirect('/login?error=invalid')

@app.route("/logout")
def logout():
    session.pop("name")
    return redirect("/")

@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    conn = sqlite3.connect('./instance/posts.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('SELECT * FROM blog_post')
    values = cur.fetchall()
    posts = [dict(value) for value in values]
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/post/<post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    conn = sqlite3.connect('./instance/posts.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM blog_post WHERE id = {post_id}')
    values = cur.fetchone()
    requested_post = dict(values)
    conn.close()

    conn = sqlite3.connect('./instance/posts.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM comments WHERE pid = {post_id}')
    values = cur.fetchall()
    comments = [dict(value) for value in values]
    conn.close()

    return render_template("post.html", post=requested_post, comments=comments)

@app.route("/add_comment", methods=['POST', 'GET'])
def add_comment():
    if 'name' not in session:
        return redirect('/register?error=comment_prohibited')
    else:
        comment_text = request.form['ckeditor']
        pid = request.args['pid']
        if len(comment_text) == 0:
            return redirect('/')
        else:
            conn = sqlite3.connect('./instance/posts.db')
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute(f"INSERT INTO comments (pid, username, comment) VALUES ({pid}, '{session['name']}', '{comment_text}')")
            conn.commit()
            conn.close()
            return redirect(f"/post/{pid}")

# TODO: add_new_post() to create a new blog post
@app.route('/new')
def new():
    if 'name' in session and session['name'] == 'AndrewSafist':
        return render_template('make-post.html')
    else:
        return 'Unauthorized.'

@app.route('/add', methods=['POST'])
def add():
    form = request.form
    today = date.today()
    conn = sqlite3.connect('./instance/posts.db')
    cur = conn.cursor()
    conn.row_factory = sqlite3.Row
    cur.execute(f"INSERT INTO blog_post (title, date, body, author, img_url, subtitle) VALUES ('{form['title']}', '{today}', '{form['ckeditor']}', '{form['author']}', '{form['url']}', '{form['subtitle']}')")
    conn.commit()
    conn.close()
    return redirect('/')

# TODO: edit_post() to change an existing blog post
@app.route('/edit/<pid>')
def edit(pid):
    if 'name' in session and session['name'] == 'AndrewSafist':
        conn = sqlite3.connect('./instance/posts.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM blog_post WHERE id = {pid}')
        values = cur.fetchone()
        print(dict(values))
        conn.close()
        return render_template('edit.html', post=dict(values), pid=pid)
    else:
        return 'Unauthorized.'

@app.route("/modify/<pid>", methods=['POST'])
def modify(pid):
    today = str(date.today())
    form = request.form
    conn = sqlite3.connect('./instance/posts.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(f"UPDATE blog_post SET title = '{form['title']}',date = '{today}', subtitle = '{form['subtitle']}', author = '{form['author']}', img_url = '{form['url']}', body = '{form['ckeditor']}' WHERE id = {pid}")
    conn.commit()
    conn.close()
    return redirect("/")

# TODO: delete_post() to remove a blog post from the database

@app.route("/delete/<pid>")
def delete_post(pid):
    if 'name' in session and session['name'] == 'AndrewSafist':
        conn = sqlite3.connect('./instance/posts.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(f'DELETE FROM blog_post WHERE id = {pid}')
        conn.commit()
        conn.close()
        return redirect('/')
    else:
        return 'Unauthorized.'

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
