import PySimpleGUI as sg
import pandas, random, string

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = pandas.read_csv("words.csv")
words = words.to_dict(orient='records')
all_words = list(map(lambda x: x[list(words[0].keys())[0]].upper(), words))
reset = True
lives = 6
already_guessed = []

layout = [[sg.Push(), sg.Text('6 lives', key='lives'), sg.Push()], [sg.Push(), sg.Text("", key='word'), sg.Push()], [sg.Push(), sg.Button('Reset Game'), sg.Push()]]
row = [sg.Push()]
for x in range(26):
    if x == 13 or x == 25:
        if x == 25:
            row.append(sg.Button("Z"))
        row.append(sg.Push())
        layout.append(row)
        row = [sg.Push()]
    row.append(sg.Button(string.ascii_uppercase[x]))

window = sg.Window('Hangman Game', size=(500, 500), layout=layout, finalize=True)

while True:
    if reset:
        for button in already_guessed:
            window[button].update(disabled=False)
        already_guessed = []
        lives = 6
        word = random.choice(all_words)
        placeholder = word
        guessed = "*" * len(word)
        reset = False
    window['word'].update(guessed)
    window['lives'].update(HANGMANPICS[lives-lives*2-1])
    if lives == 0:
        sg.PopupOK(f"You ran out of lives. The word was {word}.", keep_on_top=True)
        reset = True
    if placeholder.strip() == '':
        sg.PopupOK("You won!")
        reset = True
    event, values = window.read(timeout=1, timeout_key='timeout')
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Reset Game':
        reset = True
        continue
    else:
        if event in placeholder:
            ordered = list(enumerate(placeholder))
            indexes = list(map(lambda y: y[0], list(filter(lambda x: x[1] == event, ordered))))
            for ind in indexes:
                guessed = list(guessed)
                guessed[ind] = event
                guessed = ''.join(guessed)
            placeholder = placeholder.replace(event, ' ')
            window[event].update(disabled=True)
            already_guessed.append(event)
        elif event == 'timeout':
            pass
        else:
            lives -= 1
            window[event].update(disabled=True)
            already_guessed.append(event)
window.close()