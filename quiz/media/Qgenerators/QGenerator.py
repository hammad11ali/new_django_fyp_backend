import random
from abc import ABC, abstractmethod
from os import path
import copy


class Question:
    def __init__(self, data=None):
        self.statement = ''
        self.type = 'MCQ'
        self.options = []
        self.correct_index = 0
        self.detail = ''
        self.type = 1
        if not data == None:
            data = data.split(';')
            if data[0] == 'type1':
                self.type_1(data)
            elif data[0] == 'type2':
                self.type_2(data)
            elif data[0] == 'type3':
                self.type_3(data)

    def type_2(self, data):
        self.statement = data[1]
        self.options = [data[2], data[3], data[4], data[5]]
        self.correct_index = int(data[6])
        self.detail = data[7]
        self.type = 2

    def type_3(self, data):
        self.statement = data[1]
        self.options = [data[2], data[3], data[4], data[5]]
        self.correct_index = int(data[6])
        self.detail = data[7]
        self.type = 3

    def type_1(self, data):
        self.statement = data[1]
        self.options = [data[2], data[3], data[4], data[5]]
        self.correct_index = int(data[6])
        self.detail = data[7]
        self.type = 1

    @staticmethod
    def initiateQuestion(question):
        if question.type == 1:
            return question
        elif question.type == 2:
            # initiate values in question accoring to type 2
            newoptions = []
            q = copy.deepcopy(question)
            for option in q.options:
                while '$' in option:
                    op = option.split("(", 1)[1]
                    op = op.split(")", 1)[0]
                    op = op.split("-")
                    op = random.randint(int(op[0]), int(op[1]))
                    op1 = option[:option.index('$')]
                    if option.index(")")+1 == len(option):
                        op2 = ""
                    else:
                        op2 = option[option.index(")")+1:]
                    option = op1+str(op)+op2
                newoptions.append(option)
            q.options = newoptions

            return q
        elif question.type == 3:
            # initiate values in question accoring to type 2
            q = copy.deepcopy(question)
            vars = dict()
            statement = q.statement
            i = 1
            while "$" in statement:
                op = statement.split("(", 1)[1]
                op = op.split(")", 1)[0]
                op = op.split("-")
                op = random.randint(int(op[0]), int(op[1]))
                op1 = statement[:statement.index('$')]
                if statement.index(")")+1 == len(statement):
                    op2 = ""
                else:
                    op2 = statement[statement.index(")")+1:]
                statement = op1+str(op)+op2
                key = f"${i}"
                vars[key] = op
                i += 1
                # print(statement)
            q.statement = statement
            newoptions = []
            for option in q.options:
                evaluable = False
                while '$' in str(option):
                    evaluable = True
                    op1 = option[:option.index('$')]
                    op2 = option[option.index("$")+2:]
                    v = option[option.index('$'):option.index('$')+2]
                    option = op1+str(vars[v])+op2
                # print(option)
                if evaluable:
                    if "@" in option:
                        print("dd")
                        option.replace("@", "sqrt")
                    option = eval(option)
                newoptions.append(option)
            q.options = newoptions
            return q

    def randomize(self):
        # randomize choices
        options = self.options[:]
        choices = [0, 1, 2, 3]
        newoptions = ['', '', '', '']
        correct = self.correct_index
        print(options)
        for i in range(4):
            indexvalue = random.choice(choices)
            newoptions[indexvalue] = options[i]
            if i == self.correct_index:
                correct = indexvalue
            choices.remove(indexvalue)
        self.options = newoptions
        self.correct_index = correct
        # print(correct)


class Learning_Objective(ABC):
    def __init__(self):
        self.name = ""
        self.questions = []
        self.concept_name = ""
        self.description = ""
        self.action_verb = ""
        self.file = ""

    @abstractmethod
    def generateQuestions(self):
        pass

    def readfromfile(self):
        file_path = path.abspath(self.file)
        dir_path = path.dirname(self.file)
        f_path = path.join(dir_path, self.file)
        # f = open(f_path, 'r')
        pre = r"C:\Users\hamma\Documents\GitHub\new_django_fyp_backend\quiz\media\Qgenerators\\"
        f = open(pre+self.file)
        for line in f:
            q = Question(line)
            self.questions.append(q)

    def getQuestions(self, n):
        data = []
        for i in range(n):
            size = len(self.questions)-1
            index = random.randint(0, size)
            question = self.questions[index]
            q = Question.initiateQuestion(question)
            q.randomize()
            data.append(q)
        return data
