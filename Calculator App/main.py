import PySimpleGUI as pg

layout = [[pg.Push(), pg.Text(key='input'), pg.Push()]]
user_input = ''
equations = ['+', '-', '*', '/']

row = [pg.Push()]
for x in range(1, 11):
    if x % 3 == 1 and x != 1:
        row.append(pg.Button(equations[0], key=equations[0]))
        equations.pop(0)
    if x % 3 == 1 and x != 1:
        row.append(pg.Push())
        layout.append(row)
        row = [pg.Push()]
    if x == 10:
        layout.append([pg.Push(), pg.Button('0', key='0'), pg.Button(equations[0], key=equations[0]), pg.Push()])
        layout.append([[pg.Push(), pg.Button("Calculate", key='Calculate'), pg.Button('CE', key='CE'), pg.Button('Backspace', key='Backspace'), pg.Push()]])
    row.append(pg.Button(str(x), key=str(x)))

layout.append([pg.Push(), pg.Text('', key='Result'), pg.Push()])
window = pg.Window('Calculator', layout=layout, size=(300, 250))

while True:
    event, values = window.read()
    if event == pg.WINDOW_CLOSED:
        break
    elif event == 'Calculate':
        if len(user_input) == 0:
            pass
        try:
            window['Result'].update(f"Result: {eval(user_input)}")
        except:
            window['Result'].update("Incorrect equation!")
    elif event == 'CE':
        user_input = ''
        window['Result'].update("")
        window['input'].update('')
    elif event == 'Backspace':
        user_input = user_input[:-1]
        window['input'].update(user_input)
    else:
        user_input += event
        window['input'].update(user_input)
window.close()