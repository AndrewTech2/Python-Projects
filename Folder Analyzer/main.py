import os, pandas

filepaths = []
print("Local Folder Analyzer")
path = input("Path to analyze > ")
if not os.path.exists(path):
    print("Path not found!")
    exit()
print()
print("Folder Analysis Report:")
for subpath, directories, files in os.walk(path):
    for file in files:
        filepath = os.path.join(subpath, file)
        filepaths.append(filepath)
print(f"Total files: {len(filepaths)}")
sizes = [round(os.path.getsize(filename) / (1024*1024), 2) for filename in filepaths]
print(f"Total Storage Used: {round(sum(sizes), 2)} MB")
print()
print("Top Largest Files:")
dictionary = dict(zip(filepaths, sizes))
largest = sorted(dictionary, key=lambda x: dictionary[x], reverse=True)
count = 1
for key in largest:
    print(f'{count}. {key} - {dictionary[key]} MB')
    count += 1
    if count >= 11:
        break