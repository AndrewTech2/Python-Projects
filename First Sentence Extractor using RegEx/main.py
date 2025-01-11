import os, re

for text in os.listdir('texts'):
    with open(f"./texts/{text}", 'r') as file:
        content = file.read()
    first = re.findall(r"[A-Za-z0-9,:;()\[\]' ]+[.?!]", content)[0]
    print(first)