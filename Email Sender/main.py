import smtplib, os
from dotenv import load_dotenv
import pandas

load_dotenv()

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user='iamandrewtech@gmail.com', password=os.environ['PASSWORD'])
emails = pandas.read_excel("email_addresses.xlsx").to_dict(orient='records')
for email in emails:
    connection.sendmail(from_addr='iamandrewtech@gmail.com', to_addrs=email['Email'], msg=f'Subject: Automated Test Message for {email['First Name']} {email['Last Name']}\n\nHi! This is an automated test message.')
connection.close()