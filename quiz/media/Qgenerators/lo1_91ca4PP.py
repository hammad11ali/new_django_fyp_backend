from . import QGenerator
import random


class Learning_Objective_Recall(QGenerator.Learning_Objective):
    def __init__(self):
        QGenerator.Learning_Objective.__init__(self)
        self.name = "recall"
        self.concept_name = "Carnot Engine"
        self.action_verb = ""
        self.description = "Student should be able to recall the available heat energy of work, effeciency of petrol engine and four processess of carnot engine"
        self.generateQuestions()

    def generateQuestions(self):
        q = QGenerator.Question()
        q.statement = "The heat required to raise the temperature of one mole of the substance through 1K called"
        q.options = ['molar specelific heat',
                     'specelific heat capacity',
                     'heat capacity',
                     'specific heat']
        q.correct_index = 0
        q.detail = "None"
        self.questions.append(q)
        q.statement = "The efficiency of petrol engine is"
        q.options = ['25-30',
                     str(random.randint(5, 15))+"-" +
                     str(random.randint(16, 25)),
                     str(random.randint(30, 40))+"-" +
                     str(random.randint(36, 50)),
                     str(random.randint(50, 60))+"-" +
                     str(random.randint(60, 70)), ]
        q.correct_index = 0
        q.detail = "None"
        self.questions.append(q)

    # REGENERATE

    def getQuestions(self, n):

        data = []
        for i in range(n):
            size = len(self.questions)-1
            index = random.randint(0, size)
            question = self.questions[index]
            question.randomize()
            data.append(question)
        return data


def getInstance():
    return Learning_Objective_Recall()
