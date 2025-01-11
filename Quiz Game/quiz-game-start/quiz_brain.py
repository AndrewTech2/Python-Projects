class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = questions_list
    def next(self):
        num = self.question_number
        print(f"Question {num + 1}. {self.questions_list[num].text} > ", end="")
        ans = input("").lower()
        if ans == self.questions_list[num].answer.lower():
            print("That's right!")
            self.question_number += 1
            self.score += 1
            print()
        else:
            print(f'That\'s wrong. The right answer was {self.questions_list[num].answer}.')
            self.question_number += 1
            print()