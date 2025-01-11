import os

master = ''

for document in os.listdir('inputs'):
    with open(f"inputs/{document}", 'r') as file:
        content = file.read()
        master += content + "\n"

with open("new.txt", 'w') as new:
    new.write(master)