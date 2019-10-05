import datetime

from django.db import models
from django.utils import timezone
from django.shortcuts import get_object_or_404


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        """
        Check if question is recently published or not.
        :return: True if recently publish.
        """
        now = timezone.now()
        return now >= self.pub_date >= now - datetime.timedelta(days=1)

    def order(self):
        return self.choice_set.all().order_by('votes')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
