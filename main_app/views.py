from django.db.models import fields
from django.http import request
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from . models import Travel

# Create your views here.

class Home(LoginView):
  template_name = "home.html"

def about(request):
  return render(request, "about.html")

def travels_index(request):
  travels = Travel.objects.all()
  return render(request, "travels/index.html", {"travels" : travels})

def travels_detail(request, travel_id):
  travel = Travel.objects.get(id=travel_id)
  return render(request, "travels/detail.html", { "travel" : travel })

class TravelCreate(CreateView):
  model = Travel
  fields = "__all__"

class TravelUpdate(UpdateView):
  model = Travel
  fields = ["city", "country", "description", "date"]

class TravelDelete(DeleteView):
  model = Travel
  success_url = "/travels/"
