from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for q in question_data["results"]:
    question_bank.append(Question(q["question"], q["correct_answer"]))

quiz = QuizBrain(question_bank)
print("WELCOME TO THE ISQTB EXAM MOCK TEST")
print("Select the correct answer (a/b/c/d) for the following questions")
while quiz.still_has_question():
    quiz.next_question()
