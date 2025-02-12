import pandas
from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap5
import csv

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__, static_folder='static')
Bootstrap5(app)


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add')
def add_cafe():
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html')


@app.route('/cafes')
def cafes():
    data = pandas.read_csv("cafe-data.csv", index_col=0)
    columns = list(data.columns)
    list_of_rows = data.to_dict('records')
    print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows, columns=columns)

@app.route('/new', methods=['POST'])
def new():
    form = dict(request.form)
    cafe_data = pandas.read_csv("cafe-data.csv", index_col=0).to_dict(orient='records')
    cafe_data.append(form)
    new_data = pandas.DataFrame(cafe_data)
    new_data.to_csv('cafe-data.csv')
    return redirect('/cafes')

if __name__ == '__main__':
    app.run(debug=True)
