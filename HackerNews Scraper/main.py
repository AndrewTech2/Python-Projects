from bs4 import BeautifulSoup as bs
import requests
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    html = requests.get("https://news.ycombinator.com").text
    html2 = requests.get("https://news.ycombinator.com/?p=2").text
    soup = bs(html, 'html.parser')
    soup2 = bs(html2, 'html.parser')

    posts = soup.select('.titleline a') + soup2.select('.titleline a')
    trs = soup.select('.submission') + soup2.select('.submission')
    scores = soup.select(".score") + soup2.select(".score")
    scores_dict = {}
    row_dict = {}
    for post in posts:
        if 'http' not in post.get("href"):
            posts.remove(post)
    for score in scores:
        scores_dict[score.get('id').split("_")[1]] = int(score.text.split()[0])
    for row in trs:
        ind = trs.index(row)
        _id = row.get("id")
        post = posts[ind]
        row_dict[_id] = [f'{post.text}', post.get("href")]
    master_dict = {}
    for _id in scores_dict:
        if scores_dict[_id] < 100:
            continue
        master_dict[_id] = {'title': row_dict[_id][0], 'url': row_dict[_id][1], 'scores': scores_dict[_id]}
    master_list = []
    for key, value in master_dict.items():
        master_list.append((key, value))
    master_list.sort(key=lambda x: x[1]['scores'], reverse=True)
    master_dict = dict(master_list)
    return render_template('home.html', items=master_dict)

app.run(debug=True)