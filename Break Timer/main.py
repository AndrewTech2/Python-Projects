import datetime
import PySimpleGUI as pg
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

layout = [
    [pg.Titlebar('Break Timer')],
    [pg.Push(), pg.Text("Enter your break website (every 2 hours)"), pg.Push()],
    [pg.Push(), pg.Input(key='website'), pg.Push()],
    [pg.Push(), pg.Button("Start Timer"), pg.Push()],
    [pg.Push(), pg.Text("", key='timer'), pg.Push()]
]

window = pg.Window("Break Timer", layout=layout)
timer = False
countdown = 10  # Set a default value

while True:
    event, values = window.read(timeout=1000)

    if event == pg.WIN_CLOSED:
        break

    if event == 'Start Timer':
        timer = not timer  # Toggle the timer state
        window['Start Timer'].update("Stop Timer" if timer else "Start Timer")

        if timer:
            start_time = datetime.datetime.now()
        else:
            countdown = 10 # Reset timer on stop

    if timer:
        elapsed = (datetime.datetime.now() - start_time).seconds
        remaining = max(10 - elapsed, 0)

        hours = remaining // 3600
        minutes = (remaining % 3600) // 60
        seconds = remaining % 60
        if remaining == 0:
            options = Options()
            options.add_experimental_option('detach', True)

            driver = Chrome(options=options)
            try:
                driver.get(f"https://{values['website']}")
            except:
                print("Invalid Website!")
        window['timer'].update(f"{hours:02}:{minutes:02}:{seconds:02}")


window.close()
