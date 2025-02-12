import datetime, PySimpleGUI as pg

text = "The art of fast and accurate typing is a skill that improves with practice. Every keystroke builds muscle memory, allowing fingers to move effortlessly across the keyboard. A good typist maintains a steady rhythm, avoids unnecessary errors, and focuses on precision over speed. Over time, efficiency increases, making everyday tasks much easier. Whether writing emails, coding software, or composing essays, strong typing skills are essential. Consistency and patience are key to mastering this ability. The more you type, the better you become. So keep practicing, stay focused, and watch your speed improve!"
textfmt = ".\n".join(text.split(". "))
layout = [[pg.Titlebar('Typing Speed Test')], [pg.Push(), pg.Text(key='seconds'), pg.Push()], [pg.Push(), pg.Button('Start'), pg.Push()], [pg.Push(), pg.Text(f"Enter the following text:\n {textfmt}"), pg.Push()],
          [pg.Push(), pg.Input(disabled=True, key='text'), pg.Push()], [pg.Text("", key='result')]]

window = pg.Window('Typing Speed Test', layout=layout)
active = False

while True:
    event, values = window.read(timeout=1000)
    if event == pg.WIN_CLOSED:
        break
    if event == 'Start':
        window['Start'].update(disabled=True)
        window['text'].update(disabled=False)
        start = datetime.datetime.now()
        active = True
    if active:
        window['seconds'].update(f"{60-(datetime.datetime.now()-start).seconds} seconds left")
        if (datetime.datetime.now()-start).seconds == 60:
            active = False
            window['Start'].update(disabled=False)
            window['text'].update("", disabled=True)
            if 'text' not in values:
                window['result'].update("You didn't type anything!")
            else:
                user = values['text']
                if not text.startswith(user) and text != user:
                    window['result'].update("Incorrect text! Try again!")
                else:
                    window['result'].update(f"Your typing speed: ~{len(user.split())} words per minute")

window.close()