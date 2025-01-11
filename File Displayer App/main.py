from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    content = ''
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        if filename[-4:] != '.txt':
            content = ['Incorrect file extension. Should be: .txt.']
        file.save(f'uploads/{filename}')
        try:
            with open(f"uploads/{filename}", 'r') as file:
                text = file.read()
                content = text.split("\n")
        except:
            content = ['Error while reading file. Check its contents.']
    return render_template('home.html', content=content)

app.run(debug=True)