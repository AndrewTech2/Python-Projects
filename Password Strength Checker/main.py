import string
from nltk.corpus import words
import nltk

nltk.download("words")

password = input('Password > ')
if ' ' in password:
    print("Passwords must not contain whitespaces.")
    exit()
print()
if len(password) < 8:
    print("You should include at least 8 characters.")
count = 0
uppercase = False
lowercase = False
digit = False
special = False
for let in password:
    if let in string.ascii_uppercase:
        uppercase = True
    if let in string.ascii_lowercase:
        lowercase = True
    try:
        if int(let) in range(10):
            digit = True
    except ValueError:
        pass
    if let in ['!', '@', '$', '#', '%', '^', '&', '*']:
        special = True
if password.lower() in words.words():
    print("Your password is a common dictionary word.")
if not special:
    print("You should include at least one special character.")
    count += 1
if not lowercase or not uppercase:
    print('You should include both uppercase and lowercase letters.')
    count += 1
if not digit:
    print("You should include at least a digit.")
    count += 1
print()
if len(password) < 8 or count == 3 or password.lower() in words.words():
    strength = 'Weak'
elif count == 2:
    strength = 'Medium'
elif count == 1:
    strength = 'Strong'
else:
    strength = 'Perfect'
print(f"Password Strength: {strength}")