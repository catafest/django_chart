from django.db import models
# Post data 
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Test001(models.Model):
    name = models.CharField(max_length = 220)
    money = models.IntegerField()

    def __str__(self):
        return "{}-{}".format(self.name,self.money)

class Snippet(models.Model):
    title = models.CharField(max_length = 100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

#create a post
class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    #if the user is deleted their posts is deleted 
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    