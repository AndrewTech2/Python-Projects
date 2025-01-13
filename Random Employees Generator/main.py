import pandas, names, random

genders = ['male', 'female']
full_names = []
emails = []
ages = []
employee_genders = []

for x in range(100):
    gender = random.choice(genders)
    full_name = names.get_full_name(gender)
    full_names.append(full_name)
    ages.append(random.randint(20, 48))
    emails.append(f"{full_name.split()[0].lower()}.{full_name.split()[1].lower()}@company.com")
    employee_genders.append(gender)

df = pandas.DataFrame({'Name': full_names, 'Email': emails, 'Age': ages, 'Gender': employee_genders})
df.to_csv("employees.csv")