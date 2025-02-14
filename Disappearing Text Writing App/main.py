import datetime
import PySimpleGUI as pg

layout = [[pg.Titlebar('Disappearing Writing App')], [pg.Push(), pg.Text("Let's test your creativity! Once you stop writing, you've got 5-10 seconds until everything gets deleted."), pg.Push()], [pg.Push(), pg.Multiline(key='text', size=(75, 25)), pg.Push()]]

window = pg.Window('Disappearing Writing App', layout=layout)
start = None
text1 = ''

while True:
    event, values = window.read(timeout=1000)
    if event == pg.WINDOW_CLOSED:
        break
    if not values['text']:
        start = None
        text1 = ''
        continue
    if not start:
        start = datetime.datetime.now()
        text1 = values['text']
    else:
        t2 = datetime.datetime.now()
        if (t2-start).seconds >= 5:
            text2 = values['text']
            if text2 != text1:
                start = t2
                text1 = text2
            else:
                window['text'].update('')

window.close()