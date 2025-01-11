from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
app = Flask(__name__)
Bootstrap5(app)

@app.route('/')
def home():
    response = requests.get('https://api.sheety.co/3a29184ad8ddb9d144e36f98ad2ebac4/booksDatabase/sheet1',
                            headers={'Authorization': 'Basic QW5kcmV3VGVjaDpmZGFpajIzNGp1ZGFkZjFlMw=='})
    response.raise_for_status()
    data = response.json()
    if len(data['sheet1']) == 0:
        all_books = []
    else:
        all_books = data['sheet1']
    return render_template('index.html', books=all_books, length=str(len(all_books)))


@app.route("/add")
def add():
    return render_template('add.html')

@app.route('/post', methods=['POST'])
def post():
    form = request.form
    response = requests.post('https://api.sheety.co/3a29184ad8ddb9d144e36f98ad2ebac4/booksDatabase/sheet1', headers={'Authorization': 'Basic QW5kcmV3VGVjaDpmZGFpajIzNGp1ZGFkZjFlMw=='}, json={'sheet1': {'title': form['name'], 'author': form['author'], 'rating': form['rating']}})
    response.raise_for_status()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

