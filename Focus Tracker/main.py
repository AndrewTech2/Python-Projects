import PySimpleGUI as pg
import datetime

layout = [[pg.Titlebar('Focus Timer')], [pg.Text('Enter your task:')], [pg.Push(), pg.Input(key='task_name', size=(80, 30)), pg.Push()], [pg.Push(), pg.Button('Start session', key='start'), pg.Push()], [pg.Text("Time Elapsed: "), pg.Text("", key='time')], [pg.Text("Focusing on:"), pg.Text("", key='focusing')], [pg.Text("Completed tasks:")], [pg.Push(), pg.Multiline('', key='completed', disabled=True, size=(80, 10)), pg.Push()], [pg.Push(), pg.Button("Complete Task", key='complete', disabled=True), pg.Push()]]

completed_tasks = []
window = pg.Window('Focus Timer', layout=layout, size=(500, 500))
timer = False

while True:
    event, values = window.read(timeout=1000)
    if event == pg.WINDOW_CLOSED:
        break
    if event == 'start' and values['task_name']:
        window['start'].update(disabled=True)
        task = values['task_name']
        t0 = datetime.datetime.now()
        window['focusing'].update(values['task_name'])
        window['complete'].update(disabled=False)
        timer = True
    if timer:
        seconds = (datetime.datetime.now() - t0).seconds
        time = f'{seconds // 60}:{0 if seconds % 60 < 10 else ''}{seconds % 60}'
        window['time'].update(time)
    if event == 'complete':
        window['start'].update(disabled=False)
        final_time = (datetime.datetime.now()-t0).seconds // 60
        window['focusing'].update('')
        window['complete'].update(disabled=True)
        completed_tasks.append(f"✅ Task: {task} | Duration: {final_time} minute(s)")
        window['completed'].update("\n".join(completed_tasks))
        timer = False

window.close()