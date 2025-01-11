from flask import Flask

recipes = {
    1: {'id': 1, 'title': 'Spaghetti Carbonara', 'ingredients': ['spaghetti', 'eggs', 'pecorino cheese', 'guanciale'], 'instructions': 'Cook pasta, fry guanciale, mix with eggs and cheese, and combine with pasta.'},
    2: {'id': 2, 'title': 'Tomato Soup', 'ingredients': ['tomato', 'water', 'salt'], 'instructions': 'Boil all together until mushy, blend, and serve.'},
    3: {'id': 3, 'title': 'Grilled Cheese Sandwich', 'ingredients': ['bread', 'cheese', 'butter'], 'instructions': 'Butter bread, place cheese between slices, grill until golden.'}
}

app = Flask(__name__)

@app.route("/")
def home():
    return 'Homepage'

@app.route("/recipe/<rid>", methods=['GET'])
def recipe(rid):
    try:
        return recipes[int(rid)]
    except (ValueError, KeyError) as exc:
        return {'error': 'Invalid ID'}, 404

app.run(debug=True)