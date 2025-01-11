import pandas, smtplib, random, datetime
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

today = datetime.date.today()
email = "iamandrewtech@gmail.com"
password = "lewqeyzedapdikfu"

birthdays = pandas.read_csv('birthdays.csv')
birthdays = birthdays.to_dict()
birth_dict = {}
for index in birthdays['name']:
    temp_dict = {}
    for field in birthdays:
        if field == 'name':
            continue
        else:
            temp_dict[field] = birthdays[field][index]
    birth_dict[birthdays['name'][index]] = temp_dict

for name in birth_dict:
    if birth_dict[name]['month'] == today.month and birth_dict[name]['day'] == today.day:
        letter = random.randint(1, 3)
        with open(f"./letter_templates/letter_{letter}.txt", 'r') as file:
            content = file.read()
            content = content.replace("[NAME]", name)
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=birth_dict[name]['email'], msg=f"Subject: Happy Birthday!\n\n{content}")