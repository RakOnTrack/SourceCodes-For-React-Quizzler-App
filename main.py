from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface
import random


question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question.get("correct_answer") or question.get("answer")
    incorrect_answers = question.get(
        "incorrect_answers") or question.get("incorrect")
    new_question = Question(question_text, question_answer, incorrect_answers)
    question_bank.append(new_question)


print("there are " + str(len(question_bank)) + " questions.")
random.shuffle(question_bank)
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
