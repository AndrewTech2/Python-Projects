import PySimpleGUI as pg
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
active = False
done = 0

# ---------------------------- UI SETUP ------------------------------- #
layout=[[pg.Push(background_color=YELLOW), pg.Text("Not Started", background_color=YELLOW, text_color=RED, key = 'status', font='Courier'), pg.Push(background_color=YELLOW)],
        [pg.Push(background_color=YELLOW), pg.Image("tomato.png", background_color=YELLOW),
         pg.Push(background_color=YELLOW)],
        [pg.Push(background_color=YELLOW), pg.Text(text="00:00", font=FONT_NAME, background_color=YELLOW, text_color=RED, key='TIMER'), pg.Push(background_color=YELLOW)],
        [pg.Push(background_color=YELLOW), pg.Button(button_text='Start', key='START'), pg.Push(background_color=YELLOW), pg.Button('Stop'), pg.Push(background_color=YELLOW)],
        [pg.Push(background_color=YELLOW),  pg.Text('✅'*done, background_color=YELLOW, text_color=GREEN, key='checkmarks'), pg.Push(background_color=YELLOW)]]
screen = pg.Window(title='Pomodoro Timer', size=(400, 400), layout=layout, background_color=YELLOW)

while True:
    event, values = screen.read()
    if event == pg.WINDOW_CLOSED:
        break
    if event == "START":
        timer = 25*60
        to_go = 4
        done = 0
        screen['checkmarks'].update("✅" * done)
        break_bool = False
        long_break = False
        screen['START'].update(disabled=True)
        screen['TIMER'].update('25:00')
        active = True
        screen['status'].update("Session 1")
    if active:
        screen.timer_start(1000, repeating=False)
        timer -= 1
        screen['TIMER'].update(f'{0 if timer//60 < 10 else ''}{timer//60}:{0 if timer%60 < 10 else ''}{timer%60}')
        if timer == 0 and not break_bool and not long_break:
            done += 1
            to_go -= 1
            if to_go != 0:
                break_bool = True
                screen['status'].update("Short Break (5 minutes)")
                screen['checkmarks'].update("✅"*done)
                timer = 300
            else:
                screen['checkmarks'].update("✅" * done)
                timer = 20*60
                long_break = True
                screen['status'].update("Long Break (15 minutes)")
        elif timer == 0 and break_bool:
            break_bool = False
            screen['status'].update(f"Session {done+1}")
            timer = 25*60
        elif timer == 0 and long_break:
            screen['status'].update("Completed")
            active = False
            screen['START'].update(disabled=False)
    if event == 'Stop':
        screen['status'].update("Not Started")
        active = False
        screen['TIMER'].update("00:00")
        screen['checkmarks'].update('')
        screen['START'].update(disabled=False)
screen.close()