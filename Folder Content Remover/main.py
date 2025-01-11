import os, shutil, datetime

now = str(datetime.datetime.now()).split()
now[0] = now[0].replace('-', '')
now[1] = now[1].split(".")[0].replace(":", '')
now = ''.join(now)

if 'Backups' not in os.listdir():
    os.mkdir('Backups')

for content in os.listdir('Downloads'):
    shutil.move(f'Downloads/{content}', 'Backups')


