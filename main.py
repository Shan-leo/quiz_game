from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data["results"]:
    question_text = question["question"]
    question_answer = question["correct_answer"]

    newq = Question(question_text, question_answer)

    question_bank.append(newq)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score is {quiz.quiz_score}/{quiz.question_number}")