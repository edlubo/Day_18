class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        Number_questions = len(self.question_list)
        if self.question_number < Number_questions:
            return True
        else:
             False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer= input(f"Q.{self.question_number}:{current_question.text},  True or False? ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, u_answer, c_answer):
        if u_answer == c_answer.lower():
            print("You are right!")
            self.score += 1
            print(f"Your score is {self.score}/{self.question_number}.")
        else:
            print("That's wrong")
            print(f"Your score is {self.score}/{self.question_number}.")
        print(f"The correct asnswer was: {c_answer}.")
        print("\n")

