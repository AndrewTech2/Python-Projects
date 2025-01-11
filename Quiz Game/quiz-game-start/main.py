import question_model
from quiz_brain import QuizBrain
import requests

print("The Quiz Game")
print()

questions_dict = eval(requests.get("https://opentdb.com/api.php?amount=10").text)
questions = []
for x in questions_dict['results']:
    new_q = question_model.Question(x['question'], x["correct_answer"])
    questions.append(new_q)

process = QuizBrain(questions)
while True:
    process.next()
    print(f"Your score: {process.score}/10.")
    print()
    if process.question_number == len(questions):
        print("You have completed the quiz.")
        exit()