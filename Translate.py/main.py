import translate
with open("file.txt") as file:
    content = file.read()
translator = translate.Translator(to_lang='ro')
with open("translated.txt", 'w') as file:
    file.write(translator.translate(content))