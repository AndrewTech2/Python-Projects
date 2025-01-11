import os

# with open("snowwhite.txt", 'r') as file:
#     content = file.read()
#     sentences = content.split(".")
#     sentences = list(map(lambda x: x.strip().capitalize(), sentences))
#     corrected = '. '.join(sentences)
# with open("corrected.txt", 'w') as new:
#     new.write(corrected)

class File:
    def __init__(self, path):
        self.path = path
    def read_content(self):
        with open(self.path, 'r') as file:
            return file.read()
class Text:
    def __init__(self, string):
        self.string = string
    def capitalize_sentences(self):
        sentences = self.string.split(".")
        sentences = list(map(lambda sentence: sentence.strip().capitalize(), sentences))
        return ". ".join(sentences)

snowwhite = File("snowwhite.txt")
text = Text(snowwhite.read_content())
with open("corrected.txt", 'w') as file:
    file.write(text.capitalize_sentences())