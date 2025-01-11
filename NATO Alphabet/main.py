import pandas

nato_alphabet = pandas.read_csv("./nato_phonetic_alphabet.csv").to_dict()
nato_dict = {}
for ind in nato_alphabet['letter']:
    nato_dict[nato_alphabet['letter'][ind]] = nato_alphabet['code'][ind]
while True:
    again = False
    sentence = input("Word > ")
    output = []
    for let in sentence.upper():
        if let in nato_dict.keys():
            output.append(nato_dict[let])
        else:
            print("Sorry, your text contains non-alphabetic characters.")
            again = True
            break
    if again:
        print()
        continue
    break
print(output)