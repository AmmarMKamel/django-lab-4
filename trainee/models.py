from django.db import models
from track.models import Track


# Create your models here.
class Trainee(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    track_id = models.ForeignKey(Track, on_delete=models.CASCADE)
