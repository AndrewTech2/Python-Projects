import os
import werkzeug.security
from werkzeug.security import generate_password_hash, check_password_hash

originals = []
for filename in os.listdir('files'):
    with open(f"files/{filename}", 'rb') as file:
        content = str(file.read())
        deletion = False
        for hash_val in originals:
            if check_password_hash(hash_val, password=content):
                deletion = True
        if not deletion:
            originals.append(generate_password_hash(content, method='pbkdf2'))
    if deletion:
        os.remove(f"files/{filename}")