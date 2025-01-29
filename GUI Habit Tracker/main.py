import PySimpleGUI as pg
import os, pandas


data = []
if 'habits.json' in os.listdir():
    data = pandas.read_json('habits.json').to_dict(orient='records')

layout = [[pg.Push(), pg.Input(key='habit'), pg.Push()], [pg.Push(), pg.Button("Add Habit"), pg.Push()], [pg.Column([[]], key='habits')]]

window = pg.Window("Habit Tracker", layout=layout, finalize=True)

def update_layout():
    for habit in data:
        window.extend_layout(window['habits'], [[pg.Push(), pg.Text(f"{habit['Habit']} (Streak: {habit['Streak']})"),
                                                 pg.Button("Complete", key=f'complete-habit-{habit['Habit']}'),
                                                 pg.Push()]])
update_layout()

def recreate_window():
    data = []
    if 'habits.json' in os.listdir():
        data = pandas.read_json('habits.json').to_dict(orient='records')
    layout = [[pg.Push(), pg.Input(key='habit'), pg.Push()], [pg.Push(), pg.Button("Add Habit"), pg.Push()],
              [pg.Column([[]], key='habits')]]
    return pg.Window("Habit Tracker", layout=layout, finalize=True)

while True:
    event, values = window.read()
    if event == pg.WINDOW_CLOSED:
        break
    if event == 'Add Habit' and values['habit'] is not None:
        if len(data) != 0:
            data_df = pandas.DataFrame(data)
            if values['habit'] in data_df['Habit'].to_list():
                pg.PopupOK('ERROR: Habit already exists!')
                continue
        data.append({'Habit': values['habit'], 'Streak': 0})
        data_df = pandas.DataFrame(data)
        data_df.to_json("habits.json")
        window.close()
        window = recreate_window()
        update_layout()
    if 'complete-habit' in event:
        habit_name = event.split("-")[2]
        print(habit_name)
        data_df = pandas.DataFrame(data)
        if habit_name in data_df['Habit'].to_list():
            ind = data_df['Habit'].to_list().index(habit_name)
        data_df['Streak'][ind] += 1
        data = data_df.to_dict(orient='records')
        data_df = pandas.DataFrame(data)
        data_df.to_json("habits.json")
        window.close()
        window = recreate_window()
        update_layout()

window.close()