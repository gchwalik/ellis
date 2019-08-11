# Create your models here.
import datetime

from django.db import models

from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Lawyer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    university = models.CharField(max_length=80)
    title = models.CharField(max_length=50)
    years_of_experience = models.IntegerField(default=0)
    intro = models.CharField(max_length=300)
    f1_visa_expertise = models.BooleanField(default=False)
    f1_opt_expertise = models.BooleanField(default=False)
    green_card_expertise = models.BooleanField(default=False)
    h1B_expertise = models.BooleanField(default=False)
    price_range = models.IntegerField(default=2)
    rating = models.IntegerField(default=4)

    def __str__(self):
        return self.first_name + " " + self.last_name
   


