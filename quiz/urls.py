from django.urls import path
from .views import start_quiz, get_question, submit_answer, results

urlpatterns = [
    path('start/', start_quiz, name='start_quiz'),
    path('question/', get_question, name='get_question'),
    path('submit/', submit_answer, name='submit_answer'),
    path('results/', results, name='results'),
]