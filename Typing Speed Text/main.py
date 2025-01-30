import datetime, PySimpleGUI as pg
from turtledemo.penrose import start

text = "Python is an interpreted, high-level programming language."
layout = [[pg.Titlebar('Typing Speed Test')], [pg.Push(), pg.Button('Start'), pg.Push()], [pg.Push(), pg.Text(f"Enter the following text: {text}"), pg.Push()],
          [pg.Push(), pg.Input(disabled=True, key='text'), pg.Push()], [pg.Push(), pg.Button("Submit", disabled=True), pg.Push()], [pg.Text("", key='result')]]

window = pg.Window('Typing Speed Test', layout=layout)

while True:
    event, values = window.read(timeout=1000)
    if event == pg.WIN_CLOSED:
        break
    if event == 'Start':
        window['Start'].update(disabled=True)
        window['text'].update(disabled=False)
        window['Submit'].update(disabled=False)
        start_time = datetime.datetime.now()
    if event == 'Submit' and values['text'] == text:
        end_time = datetime.datetime.now()
        time_difference = (end_time - start_time).seconds
        print(time_difference)
        window['Start'].update(disabled=False)
        window['text'].update("", disabled=True)
        window['Submit'].update(disabled=True)
        window['result'].update(f"Your typing speed: {(len(text.split()) * 60) // time_difference} words per minute")

window.close()