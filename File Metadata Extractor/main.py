import os, datetime
import time
from datetime import timedelta
import pandas

path = input('Enter the path to analyze > ')
print()
dictionary = []
try:
    for file in os.listdir(path):
        filepath = os.path.join(path, file)
        if not os.path.isfile(filepath):
            continue
        size = os.path.getsize(filepath)
        creation = time.ctime(os.path.getctime(filepath))
        modification = time.ctime(os.path.getmtime(filepath))
        type = "." + file.split(".")[-1]
        print(f"Path: {filepath}, Size: {size} bytes, Created: {creation}, Modified: {modification}, Type: {type}")
        dictionary.append({'Path': filepath, 'Size': size, 'Created': creation, 'Modified': modification, 'Type': type})
except Exception as err:
    print(err)
else:
    save = input('Do you wish to save the data to a CSV file (y/n) > ')
    if save.lower() == 'y':
        df = pandas.DataFrame(dictionary)
        df.to_csv("metadata.csv")