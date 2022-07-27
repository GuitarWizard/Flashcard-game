from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface
# Note API endpoints are anything before the questionmark
# After teh questiomark are the different parameters

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

quiz_ui = QuizInterface(quiz)

# Note: because the mainloop in tkinter is basically a continuouse while loop
# it will be confused by the while loop below, so we commented it out.
# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
