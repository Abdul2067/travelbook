from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.db.models.aggregates import Max
from django.urls import reverse

RATING = (
  ("5", "5"),
  ("4", "4"),
  ("3", "3"),
  ("2", "2"),
  ("1", "1")
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

class Photo(models.Model):
  url = models.CharField(max_length=250)
  travel = models.OneToOneField(Travel, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for travel_id: {self.travel_id} @{self.url}"