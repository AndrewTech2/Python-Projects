import PySimpleGUI as pg
import google.generativeai as genai

genai.configure(api_key='AIzaSyCNS5oZwCN1fs3KNj60SU1dNit1YLi91iU')
model = genai.GenerativeModel('gemini-1.5-flash-latest')
layout = [[pg.Push(), pg.Text('Gemini App'), pg.Push()], [pg.Text("Enter a prompt:")], [pg.Input(key='prompt')], [pg.Button('Generate', key='Generate')], [pg.Text(visible=False, key='response')]]

window = pg.Window('Gemini App', layout=layout, size=(200, 200), finalize=True)
window.maximize()
while True:
    event, values = window.read()
    if event == pg.WINDOW_CLOSED:
        break
    if event == 'Generate':
        response = model.generate_content(values['prompt']).text
        window['response'].update(response, visible=True)
window.close()