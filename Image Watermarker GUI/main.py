from PIL import Image, ImageDraw
import PySimpleGUI as pg

layout = [[pg.Titlebar('Image Watermarker')], [pg.Push(), pg.Text("Select your image:"), pg.Push()], [pg.Push(), pg.Input(key="image"), pg.FileBrowse('Browse', key='Browse', file_types=(('Images', "*.png;*.jpeg;*.jpg"),)), pg.Push()], [pg.Push(), pg.Text("Watermark text:"), pg.Input(key='watermark'), pg.Button("Submit"), pg.Push()], [pg.Text("", key='success')]]

window = pg.Window("Image Watermarker", layout=layout)

while True:
    event, values = window.read()
    if event == pg.WINDOW_CLOSED:
        break
    if event == 'Submit' and 'image' in values and 'watermark' in values:
        img = Image.open(values['image'])
        watermark = ImageDraw.Draw(img)
        watermark.text((img.size[0]/2, img.size[1]/2), values['watermark'])
        img.save('watermarked.png')
        window['success'].update("Saved successfully!")
window.close()