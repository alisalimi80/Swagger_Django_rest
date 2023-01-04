from django.db import models 
from django.db.models import PROTECT ,CASCADE


# Create your models here.

class Writer(models.Model):

    first_name = models.CharField(max_length=120,null=False)

    last_name = models.CharField(max_length=120,null=False)

    birthday = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Cast(models.Model):

    first_name = models.CharField(max_length=120,null=False)

    last_name = models.CharField(max_length=120,null=False)

    birthday = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Movie(models.Model):

    name = models.CharField(max_length=120,null=False)

    time = models.CharField(max_length=120,null=False)

    description = models.TextField(max_length=2000,null=True,blank=True)

    country = models.CharField(max_length=120,null=False)

    language = models.CharField(max_length=120,null=False)

    writer = models.ForeignKey(Writer,on_delete=CASCADE)

    casts = models.ManyToManyField(Cast)

    def __str__(self):
        return self.name

    





