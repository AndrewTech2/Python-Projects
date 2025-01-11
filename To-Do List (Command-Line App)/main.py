import datetime

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
today = days[datetime.datetime.now().weekday()]

print("Welcome! Start by adding your tasks. Separate them with new lines. Write 'done' when done.")
tasks = []

while True:
    task = input()
    if task.lower() == 'done':
        if len(tasks) == 0:
            print("No tasks added!")
        else:
            string = "\n".join(tasks) + "\n"
            with open(f'{today}.txt', 'a') as file:
                file.write(string)
        break
    else:
        tasks.append(task)