import os, PySimpleGUI as pg

gallery = [os.path.join("Gallery", file) for file in os.listdir('Gallery')]

current = 0

layout = [[pg.Push(), pg.Image(gallery[0], key='image'), pg.Push()], [pg.Push(), pg.Button('Previous'), pg.Button("Next"), pg.Push()], [pg.Push(), pg.Button("Update Folder"), pg.Push()]]

window = pg.Window('Image Gallery Viewer', layout=layout)

while True:
    event, values = window.read()
    if event == pg.WINDOW_CLOSED:
        break
    if event == 'Previous':
        current -= 1
        if current == -1:
            current = len(gallery) - 1
        window['image'].update(gallery[current])
    elif event == 'Next':
        current += 1
        if current == len(gallery):
            current = 0
        window['image'].update(gallery[current])
    elif event == 'Update Folder':
        gallery = [os.path.join("Gallery", file) for file in os.listdir("Gallery")]
        current = 0
        window['image'].update(gallery[current])
window.close()