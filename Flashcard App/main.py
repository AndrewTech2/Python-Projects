import PySimpleGUI as pg
import pandas, random, os
from pandas.core.interchange.dataframe_protocol import DataFrame

BACKGROUND_COLOR = "#B1DDC6"

layout = [[],
          [pg.Push(background_color=BACKGROUND_COLOR), pg.Text('Flashcard App', background_color=BACKGROUND_COLOR, font='Courier', key='title'), pg.Push(background_color=BACKGROUND_COLOR)],
          [pg.Push(background_color=BACKGROUND_COLOR), pg.Text("Press any button to start", background_color=BACKGROUND_COLOR, font=('Courier', 30), key='word'), pg.Push(background_color=BACKGROUND_COLOR)],
          [pg.Push(background_color=BACKGROUND_COLOR), pg.Button('✅', font=('Courier', 20), button_color='#00ff00', key='know'), pg.Push(background_color=BACKGROUND_COLOR), pg.Button("❌", font=("Courier", 20), button_color="#FF0000", key='not know'), pg.Push(background_color=BACKGROUND_COLOR)],
          [pg.Push(background_color=BACKGROUND_COLOR), pg.Text("5", visible=False, key='timer'), pg.Push(background_color=BACKGROUND_COLOR)]
          ]
screen = pg.Window(title="Flashcard Study App", layout=layout, background_color=BACKGROUND_COLOR, finalize=True)

dataframe = pandas.read_csv("./data/french_words.csv")
dict_data = dataframe.to_dict()
dictionary = {}
if 'words_to_learn.csv' in os.listdir("./data"):
    dataframe = pandas.read_csv("./data/words_to_learn.csv")
    dict_data = dataframe.to_dict()
for index in dict_data['French'].keys():
    dictionary[dict_data['French'][index]] = dict_data['English'][index]
active = True
timer = 5
first_run = True

while True:
    event, values = screen.read()
    if event == pg.WINDOW_CLOSED:
        break
    if len(dictionary.keys()) == 0:
        pg.PopupOK("All words have been revised!")
        break
    if event == 'know':
        screen['timer'].update(visible=False)
        timer = 5
        if not first_run:
            del dictionary[french_word]
            to_revise_french = list(dictionary.keys())
            to_revise_english = list(dictionary.values())
            data_dict = {'French': to_revise_french, 'English': to_revise_english}
            data_dict = pandas.DataFrame(data_dict)
            data_dict.to_csv("./data/words_to_learn.csv")
        else:
            first_run = False

        if len(dictionary.keys()) > 0:
            french_word = random.choice(list(dictionary.keys()))
            screen['title'].update("French")
            screen['word'].update(french_word)
        active = True
    elif event == 'not know':
        first_run = False
        screen['timer'].update(visible=False)
        timer = 5
        if len(dictionary.keys()) > 0:
            french_word = random.choice(list(dictionary.keys()))
            screen['title'].update("French")
            screen['word'].update(french_word)
        active = True
    if active:
        screen.timer_start(1000, repeating=False)
        timer -= 1
        screen['timer'].update("Time left to answer:" + str(timer),visible=True)
        if timer == 0:
            screen['timer'].update(visible=False)
            screen['title'].update("English")
            screen['word'].update(dictionary[french_word])
            timer = 5
            active = False
screen.close()
