from django.shortcuts import HttpResponse
from .models import Question

def index(request):
    newest_question_list = Question.objects.order_by('-pub_date')
    output = ', '.join([q.question_text for q in newest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}.")


def result(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}.")


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
