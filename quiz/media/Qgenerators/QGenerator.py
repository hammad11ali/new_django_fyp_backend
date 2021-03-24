import random
from abc import ABC, abstractmethod


class Question:
    def __init__(self):
        self.statement = ''
        self.type = 'MCQ'
        self.options = []
        self.correct_index = 0
        self.detail = ''
    # Randomizes the options array

    def randomize(self):
        options = self.options[:]
        choices = [0, 1, 2, 3]
        newoptions = ['', '', '', '']
        correct = 0
        for i in range(4):
            indexvalue = random.choice(choices)
            newoptions[indexvalue] = options[i]
            if i == self.correct_index:
                correct = indexvalue
            choices.remove(indexvalue)
        self.options = newoptions
        self.correct_index = correct


class Learning_Objective(ABC):
    def __init__(self):
        self.name = ""
        self.questions = []
        self.concept_name = ""
        self.description = ""
        self.action_verb = ""

    @abstractmethod
    def generateQuestions(self):
        pass

    @abstractmethod
    def getQuestions(self, n):
        pass
