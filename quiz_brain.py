import html
from data import updateFileFromObjectData


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.length = len(self.question_list)
        self.current_question = None
        self.realIndex = self.question_number - self.score

    def still_has_questions(self):
        valid = self.question_number < self.length
        if not valid:
            print("your score is: " + str(self.score) + "/" + str(self.length) +
                  ". that is " + str(self.score/self.length * 100) + " percent.")
            if self.score == self.length:
                print(
                    "You got perfect! test will reset, move onto the next test or try this one again.")

        return valid

    def next_question(self):
        self.question_number += 1
        self.realIndex = self.question_number - 1 - self.score
        self.current_question = self.question_list[self.realIndex]
        q_text = html.unescape(self.current_question.question)
        return f"Q.{self.question_number}: {q_text}"

    def getChoices(self):
        return self.current_question.choices

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer != "Dont Know" and user_answer != 4:

            if self.current_question.choices[user_answer].lower() == correct_answer.lower():

                return True
        else:
            return False

    def removeQuestion_AndUpdateF(self):
        # remove question from quiz by deleting it from the array,
        self.question_list.pop(self.realIndex)
        updateFileFromObjectData(self.question_list)

    def updateFile(self):

        raw_data = self.question_list

        updateFileFromObjectData(raw_data)
