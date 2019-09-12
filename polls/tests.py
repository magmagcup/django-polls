from django.test import TestCase
from django.http import HttpResponse
from .models import Question

# Create your tests here.


# class ModelTest(TestCase):
#     """Check obj model"""
#
#     def test_question(self):
#         pass

newest_question_list = Question.objects.order_by('-pub_date')
output = ', '.join([q.question_text for q in newest_question_list])

print(output)
