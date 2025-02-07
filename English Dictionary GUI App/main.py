import PySimpleGUI as pg
import json

layout = [[pg.Titlebar("English Dictionary App")], [pg.Push(), pg.Input(key='word'), pg.Button("Define"), pg.Push()], [pg.Text(key='definitions')]]

window = pg.Window('English Dictionary App', layout=layout)

while True:
    event, values = window.read()
    if event == pg.WINDOW_CLOSED:
        break
    if event == 'Define' and values:
        with open("data.json", 'r') as file:
            data = json.load(file)
        word = values['word']
        if word in data:
            definitions = data[word]
            window['definitions'].update("\n".join(definitions))
        else:
            window['definitions'].update("Not found!")

window.close()
