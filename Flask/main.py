from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def index():
    with open("index.html", 'r') as file:
        content = file.read()
    return content

num = random.randint(1, 10)
print(num)

@app.route('/<int:guess>')
def number(guess):
    if guess == num:
        with open("right.html") as file:
            content = file.read()
        return content
    with open('wrong.html') as file:
        content = file.read()
    if guess < num:
        content = content.replace("{value}", 'low')
    else:
        content = content.replace("{value}", 'high')
    return content

app.run(host='0.0.0.0', port=81, debug=True)