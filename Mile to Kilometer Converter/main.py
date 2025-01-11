import PySimpleGUI as pg

conv = 1.609

layout = [[pg.Text('Mile to Kilometre Converter', key='TEXT')], [pg.Text('Number of miles > '), pg.InputText()], [pg.Button('Convert!')]]
window = pg.Window(title='Hello World', layout=layout, margins=(100,50))
total_values = []

while True:
    event, values = window.read()
    if event == 'OK' or event == pg.WIN_CLOSED:
        break
    if event == 'Convert!':
        print(total_values)
        if len(total_values) == 0:
            kilometres = [pg.Text(str(values[0]), key='KILO')]
            layout.append(kilometres)
            window.extend_layout(window, [kilometres])
            total_values.append(values)
        if len(total_values) > 0:
            total_values.append(values)
            window['KILO'].update(str(round(int(total_values[-1][0])/conv, 2)))


window.close()