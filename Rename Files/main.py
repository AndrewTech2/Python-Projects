import os, datetime

today = f"{datetime.datetime.now().year}-{datetime.datetime.now().month}-{datetime.datetime.now().day}"

for file in os.listdir('files'):
    os.rename(f"./files/{file}", f'./files/{file[:-4]}-{today}.txt')
    print(f"Renamed {file} to {file[:-4]}-{today}.txt")