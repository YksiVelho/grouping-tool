from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=200)
    maxsize = models.IntegerField()
    course_code = models.CharField(max_length=15)
    type = models.CharField(max_length=50)
    students = ArrayField(models.IntegerField())
