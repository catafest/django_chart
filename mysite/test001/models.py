from django.db import models
<<<<<<< HEAD
# Post data 
from django.utils import timezone
from django.contrib.auth.models import User
=======
>>>>>>> bc492a65a1567cf79182a4058a9a92bce2c4e73f
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
<<<<<<< HEAD

#create a post
class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    #if the user is deleted their posts is deleted 
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    
=======
>>>>>>> bc492a65a1567cf79182a4058a9a92bce2c4e73f
