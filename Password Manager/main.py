import PySimpleGUI as pg
import string, random, os
import json

WHITE = "#000000"

if 'passwords.json' in os.listdir():
    with open("passwords.json") as file:
        data = json.load(file)
else:
    data = {}
layout=[[pg.Push(), pg.Image("./logo.png"), pg.Push()],
        [pg.Push(), pg.Text("Website:"), pg.Input(key="website"), pg.Push(), pg.Button("Search"), pg.Push()],
        [pg.Push(), pg.Text("Email/Username:"), pg.Input(key='user'), pg.Push()],
        [pg.Push(), pg.Text("Password:"), pg.Input(key='password'), pg.Push(), pg.Button("Generate"), pg.Push()],
        [pg.Push(), pg.Button("Add"), pg.Push()]]
window = pg.Window(title='Password Manager', layout=layout, size=(500, 500))

while True:
    event, values = window.read()
    if event == pg.WINDOW_CLOSED:
        break
    if event == 'Generate':
        alpha = list(string.ascii_letters)  + list(string.punctuation) + [str(number) for number in range(10)]
        length = random.randint(10, 20)
        password = ''
        for x in range(length):
            password += random.choice(alpha)
        window['password'].update(password)
    if event == 'Add':
        if len(values['website']) == 0:
            pg.PopupOK("Field 'Website' is incomplete!", title='Error')
        elif len(values['user']) == 0:
            pg.PopupOK("Field 'Username/Email' is incomplete!", title='Error')
        elif len(values['password']) == 0:
            pg.PopupOK("Field 'Password' is incomplete!", title='Error')
        else:
            confirmation = pg.popup_yes_no("Are you sure these are the right details?", title="Are you sure?")
            if confirmation == 'Yes':
                data[values['website']] = {'user': values['user'], 'password': values['password']}
                with open("passwords.json", "w") as file:
                    json.dump(data, file)
                pg.PopupOK("Values added!", title='Notice')
            else:
                pass
    if event == 'Search':
        if len(values['website']) == 0:
            pg.PopupOK("Field 'Website' is incomplete!", title='Error')
        elif len(data.keys()) == 0:
            pg.PopupOK("No data added!", title='Error')
        else:
            if values['website'] in data.keys():
                pg.PopupOK(f"Username: {data[values['website']]['user']}\nPassword: {data[values['website']]['password']}", title='Search complete')
            else:
                pg.PopupOK("Website not in stored data!", title='Error')
window.close()