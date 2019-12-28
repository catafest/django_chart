from django.db import models
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
