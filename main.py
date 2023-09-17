from data import science, general_knowledge
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
user_choice = input("Which questions you want? general / science? ").lower()

if user_choice == "general":
    quiz_questions = general_knowledge
    print(f"General knowledge mode selected")
elif user_choice == "science":
    quiz_questions = science
    print(f"Science mode selected")

for question in quiz_questions:
    question_text = question["text"]
    answer = question["answer"]
    new_question = Question(question_text, answer)
    question_bank.append(new_question)
quiz = QuizBrain(question_bank)
quiz.quiz_start()
while quiz.has_questions_still():
    quiz.next_question()
if quiz.win_or_lose():
    print("You passed")
else:
    print("YOu failed")


