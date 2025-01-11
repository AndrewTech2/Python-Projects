from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
import requests


key = 'bbbf99d8096dfaf65ef163c0b6e8cbb6'
response = requests.get('https://api.themoviedb.org/3/search/movie', params={'query': 'avatar', 'api_key': key})
response.raise_for_status()
films = response.json()
print(films)
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
app = Flask(__name__, static_folder="static")
Bootstrap5(app)


@app.route("/")
def home():
    response = requests.get('https://api.sheety.co/3a29184ad8ddb9d144e36f98ad2ebac4/top10Movies/sheet1')
    response.raise_for_status()
    data = response.json()['sheet1']
    return render_template("index.html", data=data)

@app.route("/edit/<id>")
def edit(id):
    return render_template('edit.html', cid=id)

@app.route('/update/<id>', methods=['POST'])
def update(id):
    form = request.form
    response = requests.put(f'https://api.sheety.co/3a29184ad8ddb9d144e36f98ad2ebac4/top10Movies/sheet1/{id}', json={'sheet1': {'title': form['title'], 'description': form['description']}})
    response.raise_for_status()
    return redirect('/')

@app.route('/delete/<id>')
def delete(id):
    response = requests.delete(f'https://api.sheety.co/3a29184ad8ddb9d144e36f98ad2ebac4/top10Movies/sheet1/{id}')
    return redirect("/")

@app.route('/add')
def add():
    return render_template("add.html")

@app.route('/select/<title>')
def select(title):
    response = requests.get('https://api.themoviedb.org/3/search/movie', params={'query': title, 'api_key': key})
    response.raise_for_status()
    films = response.json()
    return render_template('select.html', films=films['results'])

@app.route('/process', methods=['POST'])
def process():
    title = request.form['title']
    return redirect(f'/select/{title}')

@app.route("/rate", methods=['GET'])
def rate(film):
    global local_film
    local_film = film
    return render_template('rate.html')

@app.route('/append', methods=['POST'])
def append():
    form = request.form
    card = {"title": local_film['original_title'], 'year': local_film['release_date'].split('-')[0], 'description': local_film['overview'], 'rating': form['rating'], 'review': form['review'], 'url': f'https://image.tmbd.org/t/p/w500/{local_film["poster_path"]}'}
    return card

if __name__ == '__main__':
    app.run(debug=True)
