from . import QGenerator
# import QGenerator
import random


class Learning_Objective_Recall(QGenerator.Learning_Objective):
    def __init__(self):
        super().__init__()
        self.name = "recall"
        self.concept_name = "Equilbrium"
        self.action_verb = ""
        self.file = 'carnot.txt'
        self.description = "Student should be able to recall equailibrium"
        self.generateQuestions()

    def generateQuestions(self):
        self.readfromfile()


def getInstance():
    return Learning_Objective_Recall()
