import requests
from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    books = []
    if request.method == 'POST':
        books = requests.get("https://www.googleapis.com/books/v1/volumes", params={'q': request.form['book']}).json()['items']
    return render_template('index.html', books=books)

app.run(host='0.0.0.0', port=81, debug=True)