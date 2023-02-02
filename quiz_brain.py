# attribute : question_number = 0, question_list, score = 0
# method : next_question(), still_has_question(), check_answer()

class QuizBrain:
    def __init__(self, q_list):
        self.q_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.q_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.q_number]
        self.q_number += 1
        user_input = input(f"Q.{self.q_number}: {current_question.text} (True/False): ")
        self.check_answer(user_input, current_question.answer)

    def check_answer(self, user_input, correct_answer):
        if user_input.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1

        else:
            print("That's wrong.")
        print(f"The correct answer was : {correct_answer}.")
        print(f"Your current score is {self.score}/{self.q_number}")
        print("\n")