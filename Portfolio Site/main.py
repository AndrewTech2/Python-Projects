from flask import Flask, render_template, request
import requests

app = Flask(__name__, static_folder='static')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/message", methods=['POST'])
def message():
    form = request.form
    response = requests.post("https://ntfy.sh/andrei_ivan_portfolio", data=f"You've got a new message!\nName: {form['name']}\nEmail: {form['email']}\nSubject: {form['subject']}\nMessage: {form['message']}")
    return render_template('submitted.html')

app.run(debug=True)