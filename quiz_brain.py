class QuizBrain:

    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.quiz_length = 0
    def next_question(self):
        if self.quiz_length>0 and len(self.question_list)>0:
            current_question = self.question_list[self.question_number]
            self.question_number+=1
            user_answer= input(f"{self.question_number}: {current_question.text}").title()
            self.check_answer(user_answer, current_question.answer)
            self.quiz_length  -= 1
            self.print_score()

    def has_questions_still(self):
        return self.quiz_length>0

    def quiz_start(self):
        self.quiz_length  = int(input("How many questions you want in the quiz? "))
        self.x= self.quiz_length

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print("You got it right")
            return True
        else:
            print("You got it wrong")
            return False

    def print_score(self):
        print(f"Your score = {self.score} / {self.x}")

    def win_or_lose(self):
        return self.score > self.x/2
