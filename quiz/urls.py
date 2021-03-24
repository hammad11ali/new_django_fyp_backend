from django.urls import path
from .views import *
urlpatterns = [
    path('lo/', LearningObjective_View.as_view()),
    path('quiz/', Quiz_View.as_view()),
]
