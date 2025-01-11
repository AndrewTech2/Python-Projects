import PySimpleGUI as psg
import os, time, datetime

layout = [[psg.Push(), psg.Text("Directory to Monitor:"), psg.Push()], [psg.Push(), psg.Input('Directory...', key='directory'), psg.Push()], [psg.Push(), psg.Button("Start Monitoring", key='start'), psg.Push()], [psg.Text("Unable to find directory!", key='error', visible=False)], [psg.Column(layout=[], key='log')]]

window = psg.Window('File Change Monitor', layout=layout, size=(500,500))
directory = False

while True:
    events, values = window.read(timeout=0)
    if events == psg.WINDOW_CLOSED:
        break
    if events == 'start':
        window['error'].update(visible=False)
        if not os.path.exists(values['directory']):
            window['error'].update(visible=True)
        else:
            window['start'].update(disabled=True)
            directory_path = values['directory']
            directory = True
            window['error'].update("Monitoring!", visible=True)
            window['directory'].update(disabled=True)
    if directory:
        monitor = set(os.listdir(directory_path))
        window.timer_start(frequency_ms=3000)
        new_monitor = set(os.listdir(directory_path))
        new_files = new_monitor.difference(monitor)
        deleted_files = monitor.difference(new_monitor)
        if len(new_files) != 0:
            for file in list(new_files):
                window.extend_layout(window['log'], [[psg.Push(), psg.Text(f"{file} added at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}."), psg.Push()]])
        if len(deleted_files) != 0:
            for file in list(deleted_files):
                window.extend_layout(window['log'], [[psg.Push(), psg.Text(f"{file} deleted / moved at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}."), psg.Push()]])
window.close()