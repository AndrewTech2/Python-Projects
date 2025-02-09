import google.generativeai as genai
from flask import Flask, session, render_template, request
from flask_bootstrap import Bootstrap5


genai.configure(api_key='AIzaSyCNS5oZwCN1fs3KNj60SU1dNit1YLi91iU')
model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)
app.secret_key = 'sgdijasdgijsdgasdgaj'
bootstrap = Bootstrap5(app)

@app.route("/", methods=['POST', 'GET'])
def index():
    if 'name' not in session:
        session['name'] = []
    if request.method == 'POST':
        session['name'].append({"author": 'user', 'message': request.form['query']})
        response = model.generate_content(request.form['query']).text
        session['name'].append({'author': 'ai', 'message': response})
    return render_template("home.html", messages=list(session['name']))

app.run(debug=True)