import requests

data = requests.get('https://raw.githubusercontent.com/arditsulceteaching/hosted_files/main/geo.json')
data.raise_for_status()
countries = data.json()

qid = int(input("Question ID > "))

for quiz in countries['quizzes']:
    for question in quiz['questions']:
        if question['id'] == qid:
            for choice in question['choices']:
                if question['choices'][choice]:
                    print(f"The correct answer is: {choice}")
                    exit()
print("Not found.")