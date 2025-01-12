import re

emails = []
with open("text.txt", 'r') as file:
    text = file.read()
text_list = text.split()
for word in text_list:
    if re.match(r'[-A-Za-z0-9!#$%&*+/=?^_`{|}~]+(?:\.[-A-Za-z0-9!#$%&*+/=?^_`{|}~]+)*@(?:[A-Za-z0-9](?:[-A-Za-z0-9]*[A-Za-z0-9])?\.)+[A-Za-z0-9](?:[-A-Za-z0-9]*[A-Za-z0-9])?', word):
        emails.append(word)
numbers = re.findall(r'\(?\d{3}\)?[-.]?\s?\d{3}[-.]?\d{4}', text)
print(emails)
print(numbers)