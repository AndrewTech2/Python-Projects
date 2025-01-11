import pwnedpasswords

password = input("Password to check > ")
if pwnedpasswords.check(password) == 0:
    print("Congratulations! This password has never been pwned.")
else:
    print(f"Oh no! Your password has been pwned {pwnedpasswords.check(password)} times.")