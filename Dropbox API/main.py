import os, dropbox

d = dropbox.Dropbox(oauth2_access_token='sl.CDYo7PNek5qugNjiH2YVKAHhYnlDptGAQa-bS7DLliaYheQN1R6yqgfbDWnhTSdttor7K3ktpL4XIlpwG-fs8kdFcHHi33LVuC_Tu7BWs_a4FSZ7fRqEv2xDftuvWj15llncIqFYS68z')

for image in os.listdir("images"):
    with open(f'./images/{image}', 'rb') as file:
        content = file.read()
        d.files_upload(content, f'/{image}')
        print(f"Uploaded {image}")