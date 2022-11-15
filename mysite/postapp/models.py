from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class MyPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'../../{self.pk}/detail/'

class UserInfo(models.Model):
    author = models.TextField()
    identity = models.TextField()
    info = models.TextField()
    optical_contact_info = models.TextField()
    avatar = models.TextField(default=0)

    def __str__(self):
        return self.author

class Friend(models.Model):
    name1 = models.TextField()
    name2 = models.TextField()
    def __str__(self):
        return self.name1+"&"+self.name2