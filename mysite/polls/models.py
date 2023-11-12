from django.db import models
from django.utils import timezone
import datetime
from django.contrib import admin


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    quation_details = models.TextField(
        blank=True, help_text="Enter a brief reason for the importance of this question here."
    )

    # useful when dealing with the interactive prompt, but also because objects’ 
    # representations are used throughout Django’s automatically-generated admin
    def __str__(self):
        return self.question_text
    
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    
    # You can define any function and call them upon an object of this class
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def was_published_recently_v2(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    
class Choice(models.Model):
    # each Choice is related to a single Question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text