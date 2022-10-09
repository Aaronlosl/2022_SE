from django.db import models

# Create your models here.

class User(models.Model):
     user_name = models.CharField(max_length=30)
     password = models.CharField(max_length=30)
     email = models.CharField(max_length=200)


'''
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
'''