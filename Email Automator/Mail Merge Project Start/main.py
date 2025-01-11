import os
#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

names = []
with open("/Users/iaman/PycharmProjects/Email Automator/Mail Merge Project Start/Input/Names/invited_names.txt", 'r') as f:
    contents = f.readlines()
    for x in contents:
        x = x.replace('\n', '')
        names.append(x)
with open("./Input/Letters/starting_letter.txt", 'r') as f:
    starter = f.read()
starter = starter.replace('Angela', 'Andrei I.')
for x in names:
    email = starter.replace('[name]', x)
    with open(f"./Output/ReadyToSend/{x}_email.txt", 'w') as f:
        f.write(email)
print("Emails done!")