import pandas

decoder_file = pandas.read_csv("morse_code.csv")
text = input('Sentence > ').upper()
translation = ''
for char in text:
    if char == ' ':
        translation += '/'
    if char not in decoder_file['char'].to_dict().values():
        continue
    rule = decoder_file[decoder_file['char'] == char]['code']
    rule = rule.reset_index()
    translation += rule.iloc[0]['code'] + ' '

print(translation)