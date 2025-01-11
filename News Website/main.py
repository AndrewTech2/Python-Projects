from flask import Flask, render_template
import requests

app = Flask(__name__)
api_key = '5ee9fbf933084948912d89f68738a998'

@app.route("/")
def home():
    data = requests.get(f"https://newsapi.org/v2/top-headlines?apiKey={api_key}&q=business").json()
    articles = data['articles']
    return render_template('home.html', articles=articles)

app.run(debug=True)