from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.db.models.aggregates import Max
from django.urls import reverse

RATING = (
  ("1", "5"),
  ("2", "4"),
  ("3", "3"),
  ("4", "2"),
  ("5", "1")
)
# Create your models here.
class Travel(models.Model):
  city = models.CharField(max_length=100)
  country = models.CharField(max_length=100)
  description = models.TextField(max_length=400)
  date = models.DateField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.city

  def get_absolute_url(self):
    return reverse("travels_detail", kwargs={"travel_id": self.pk})
  
class Activity(models.Model):
  activity = models.CharField(max_length=100)
  rating = models.CharField(
    max_length=1,
    choices=RATING,
    default=[0][0]
  )
  travel = models.ForeignKey(Travel, on_delete=models.CASCADE)

  def __str__(self):
    return self.activity