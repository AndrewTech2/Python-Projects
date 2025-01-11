import sys
import datetime

arguments = sys.argv
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

if len(sys.argv) != 2:
    print("Incorrect arguments. Usage: dayOfWeek.py {date in this format: YYYY-MM-DD}")
else:
    user_inp = arguments[1].split("-")
    try:
        date = datetime.date(year=int(user_inp[0]), month=int(user_inp[1]), day=int(user_inp[2]))
    except ValueError:
        print("Incorrect arguments. Usage: dayOfWeek.py {date in this format: YYYY-MM-DD}")
    else:
        print(f"The day of the week for {arguments[1]} is {weekdays[date.weekday()]}.")