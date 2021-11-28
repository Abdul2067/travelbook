from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse

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
  