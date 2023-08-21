import random
import copy


class Question:

    def __init__(self, q_text, q_answer, q_incorrect):
        self.question = q_text
        self.answer = q_answer
        self.incorrect = q_incorrect

        if len(q_incorrect) < 3:
            for i in range(3 - len(q_incorrect)):
                self.incorrect.append(' ')

        # add the correct answer to incorrect to have array of all choices
        # we make a deep copy because it would just add the answer to the incorrect answers if we dont.
        self.choices = copy.deepcopy(q_incorrect)
        self.choices.append(q_answer)
        random.shuffle(self.choices)
