from django.db import models


# Create your models here.
class Instructor(models.Model):
    name = models.CharField(max_length=255)
    salary = models.IntegerField()
    birth_date = models.DateField()
