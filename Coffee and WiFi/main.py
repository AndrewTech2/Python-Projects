from ensurepip import bootstrap
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
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)

@app.route('/new', methods=['POST'])
def new():
    form = dict(request.form)
    with open('cafe-data.csv', encoding='utf8') as file:
        data = csv.reader(file)
        list_of_rows = []
        for row in data:
            list_of_rows.append(row)
    csv_data = {}
    for header in list_of_rows[0]:
        ind = list_of_rows[0].index(header)
        header_list = []
        for row in list_of_rows[1:]:
            header_list.append(row[ind])
        header_list.append(form[header])
        csv_data[header] = header_list
    csv_data = pandas.DataFrame(csv_data)
    csv_data.to_csv('cafe-data.csv')
    return redirect('/cafes')

if __name__ == '__main__':
    app.run(debug=True)
