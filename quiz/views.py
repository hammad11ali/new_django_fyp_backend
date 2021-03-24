from django.shortcuts import render
from .models import LearningObjective
from rest_framework.views import APIView
from rest_framework.response import Response
import os
from importlib import import_module
from django.forms.models import model_to_dict
import json
# Create your views here.


class LearningObjective_View(APIView):

    def post(self, request, format=None):
        name = request.data['name']
        description = request.data['description']
        concept_name = request.data['concept_name']
        action_verb = request.data['action_verb']
        File = request.data['file']
        LearningObjective.objects.create(
            name=name, description=description, concept_name=concept_name, action_verb=action_verb, qgenerator=File)
        print("saved")
        return Response({'message': 'done'})

    def get(selt, request, format=None):
        LearningObjectives = LearningObjective.objects.all()
        contents = []
        for lo in LearningObjectives:
            t = model_to_dict(lo)
            contents.append(t)
        return Response({'Content': contents})


class Quiz_View(APIView):
    def generate(self, lo_id, n):
        lo = LearningObjective.objects.filter(id=lo_id).values()[0]
        file_ = os.path.basename(lo['qgenerator'])
        filename = os.path.splitext(file_)[0]
        modulename = '..'+filename
        QGenerator = import_module(
            modulename, package='quiz.media.Qgenerators.')
        Questions = []
        instance = QGenerator.getInstance()
        Questions = instance.getQuestions(n)
        Questions = [(q.__dict__) for q in Questions]
        return Questions

    def get(self, request, format=None):
        Content = []
        if 'id' in request.query_params.keys():
            lo_id = request.query_params['id']
            n = request.query_params['n']
            n = int(n)
            # print(lo_id,  n)
            Content = self.generate(lo_id, n)
        print(Content)

        return Response({'Content': Content})
