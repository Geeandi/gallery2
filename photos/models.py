from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.

class Album(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField(default=datetime.now)
    owner = models.IntegerField('Owner', blank=False, default=1)
    description = models.CharField(max_length=500, blank=True, null=True)
    users = models.ManyToManyField(User, blank=False)

    def __str__(self):
        return self.name

class Photo(models.Model):
    name = models.CharField(max_length=250)
    file = models.ImageField(upload_to='file/')
    date = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)
    album = models.ForeignKey(Album, blank=False, null=False, on_delete=models.CASCADE)
    description = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name
