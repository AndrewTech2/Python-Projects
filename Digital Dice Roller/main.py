import random, PySimpleGUI as pg

layout = [[pg.Titlebar('Digital Dice Roller')], [pg.Push(), pg.Text("Select the number of sides for the dice:"), pg.Push()], [pg.Push(), pg.InputOptionMenu([4, 6, 8, 10, 12, 20, 100], default_value=6, key='option'), pg.Push()], [pg.Push(), pg.Button("Roll"), pg.Push()], [pg.Push(), pg.Text('', key='roll'), pg.Push()]]

window = pg.Window('Dice Roller', layout=layout)

while True:
    event, values = window.read()
    if event == pg.WINDOW_CLOSED:
        break
    if event == 'Roll':
        window['roll'].update(f"🎲 You rolled: {random.randint(1, int(values['option']))} 🎲")

window.close()