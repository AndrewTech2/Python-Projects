import os, datetime, time

print("File Age Analyzer")
print()
path = input("Path to analyze > ")
print()
print("Analysis Report:")
recent_files = 0
medium_files = 0
old_files = 0
files = {}
for file in os.listdir(path):
    filepath = os.path.join(path, file)
    if not os.path.isfile(filepath):
        continue
    creation = datetime.datetime(year=1970, month=1, day=1) + datetime.timedelta(seconds=os.path.getctime(filepath))
    today = datetime.datetime.now()
    difference = today - creation
    files[filepath] = creation
    if difference.days <= 7:
        recent_files += 1
    elif difference.days <= 30:
        medium_files += 1
    else:
        old_files += 1
print(f"Files created less than a week ago: {recent_files}")
print(f"Files created between a week and a month ago: {medium_files}")
print(f"Files created more than a month ago: {old_files}")
print(f"Oldest file: {min(files, key=lambda x: files[x])} (Created on {files[min(files, key=lambda x: files[x])]})")
print(f"Newest file: {max(files, key=lambda x: files[x])} (Created on {files[max(files, key=lambda x: files[x])]})")