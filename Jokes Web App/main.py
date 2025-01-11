from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
import pyjokes

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html', joke=None)

@app.route("/get_joke", methods=['POST'])
def get_joke():
    joke = pyjokes.get_joke()
    return render_template("index.html", joke=joke)

app.run(debug=True)