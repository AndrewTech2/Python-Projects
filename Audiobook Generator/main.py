import pypdf, gtts

reader = pypdf.PdfReader('somatosensory.pdf')
text = ''
for page in reader.pages:
    text += "\n" + page.extract_text()

tts = gtts.gTTS(text, lang='en')
print("Hold on, the conversion process might take a bit...")
tts.save("speech.mp3")