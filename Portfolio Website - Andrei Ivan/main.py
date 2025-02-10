from flask import Flask, render_template
import pandas

education = pandas.read_csv("education.csv").to_dict("records")
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html', education = education)

app.run(debug=True)