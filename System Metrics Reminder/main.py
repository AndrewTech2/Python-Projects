import psutil, smtplib, dotenv, os, datetime

now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

dotenv.load_dotenv()
password = os.environ['PASSWORD']

cpu_usage = psutil.cpu_percent(interval=1)
total_memory = psutil.virtual_memory().total / (1024 * 1024)
used_memory = psutil.virtual_memory().used / (1024 * 1024)
total_disk = psutil.disk_usage("C:").total / (1024 * 1024 * 1024)
used_disk = psutil.disk_usage("C:").used / (1024 * 1024 * 1024)

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user='iamandrewtech@gmail.com', password=password)
connection.sendmail(from_addr='iamandrewtech@gmail.com', to_addrs='iamandrewtech@gmail.com', msg=f'''Subject: System Stats

Timestamp: {now}
CPU Usage: {cpu_usage}%
Total Memory: {total_memory} MB
Used Memory: {used_memory} MB
Total Disk Space: {total_disk} GB
Used Disk Space: {used_disk} GB

Regards,
Andrei's Python Script''')
connection.close()