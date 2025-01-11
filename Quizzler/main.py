import requests, PySimpleGUI as pg
import html, time

question_bank = requests.get("https://opentdb.com/api.php", params={'amount': 10, 'type': 'boolean'})
question_bank.raise_for_status()
question_bank = question_bank.json()
question_list = {}
for x in question_bank['results']:
    question_list[x['question']] = x['correct_answer']
count = 0
score = 0
question = html.unescape(list(question_list.keys())[count])

layout = [[pg.Text("Quizzler™️", font=('Courier', 10))],
          [pg.Push(), pg.Frame('', [[pg.Push(), pg.Text("Question 1", font=('Courier', 25), key="question title"), pg.Push()], [pg.Push(), pg.Text(question, font="Courier", key='question'), pg.Push()]], key='frame'), pg.Push()],
          [pg.Push(), pg.Button("✅", button_color="#00FF00", key='True', font=('Courier', 50)), pg.Push(), pg.Button("❌", button_color='#FF0000', key='False', font=('Courier', 50)), pg.Push()],
          [pg.Push(), pg.Text("Score: 0", font="Courier", key='score')]]
screen = pg.Window(title="Quizzler App", layout=layout, finalize=True)
screen.maximize()

while True:
    event, values = screen.read()
    if event == pg.WINDOW_CLOSED:
        break
    if event == question_list[list(question_list.keys())[count]]:
        score += 1
        count += 1
    else:
        count += 1
    if count == 10:
        screen['score'].update(f"Score: {score}")
        pg.PopupOK(f"Quiz finished! Your score was {score}.")
        break
    screen['question title'].update(f'Question {count+1}')
    screen['score'].update(f"Score: {score}")
    screen['question'].update(html.unescape(list(question_list.keys())[count]))
screen.close()