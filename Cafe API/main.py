from flask import Flask, jsonify, render_template, request
import sqlite3, random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route('/random', methods=['GET'])
def random_cafe():
    conn = sqlite3.connect('./instance/cafes.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cafe')
    values = cursor.fetchall()
    choice = random.choice(values)
    conn.close()
    return {"cafe": dict(choice)}

@app.route('/all', methods=['GET'])
def all_cafes():
    conn = sqlite3.connect('./instance/cafes.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cafe')
    values = cursor.fetchall()
    conn.close()
    return {'all_cafes': [dict(value) for value in values]}

@app.route('/search', methods=['GET'])
def search():
    location = request.args['loc']
    conn = sqlite3.connect('./instance/cafes.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM cafe WHERE location = '{location.title()}'")
    values = cursor.fetchall()
    conn.close()
    return {location.title(): [dict(value) for value in values]}

# HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def add():
    form = request.form
    conn = sqlite3.connect('./instance/cafes.db')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO cafe (name, map_url, img_url, location, has_sockets, has_toilet, has_wifi, can_take_calls, seats, coffee_price) VALUES ('{form["name"]}', '{form['map_url']}', '{form['img_url']}', '{form['location']}', '{form['has_sockets']}', '{form['has_toilet']}', '{form['has_wifi']}', '{form['can_take_calls']}', '{form['seats']}', '{form['coffee_price']}')")
    conn.commit()
    conn.close()
    return {'response': 'Successfully added coffee!'}

# HTTP PUT/PATCH - Update Record
@app.route('/update-price/<cafe_id>', methods=['PATCH'])
def update_price(cafe_id):
    new_price = request.args['new_price']
    conn = sqlite3.connect('./instance/cafes.db')
    cursor = conn.cursor()
    try:
        cursor.execute(f"UPDATE cafe SET coffee_price = '{new_price}' WHERE id = {cafe_id}")
    except:
        return {'response': 'ID not found!'}
    conn.commit()
    conn.close()
    return {'response': 'Successfully edited!'}

# HTTP DELETE - Delete Record
@app.route('/delete_cafe/<cafe_id>', methods=['DELETE'])
def delete_cafe(cafe_id):
    arguments = request.args
    if arguments['api-key'] != 'TopSecret':
        return {'error': 'Api Key not authorized.'}
    else:
        conn = sqlite3.connect('./instance/cafes.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        try:
            cur.execute(f'DELETE FROM cafe WHERE id = {cafe_id}')
        except:
            return {'error': 'ID not found!'}
        conn.commit()
        conn.close()
        return {'response': 'Successfully deleted!'}


if __name__ == '__main__':
    app.run(debug=True)
