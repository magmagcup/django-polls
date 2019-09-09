from django.shortcuts import HttpResponse
from .models import Question


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

