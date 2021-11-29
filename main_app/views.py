from django.db.models import fields
from django.http import request
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from . models import Travel
from .forms import ActivityForm

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
  activity_form = ActivityForm()
  return render(request, "travels/detail.html", { "travel" : travel, "activity_form" : activity_form })

class TravelCreate(CreateView):
  model = Travel
  fields = "__all__"

class TravelUpdate(UpdateView):
  model = Travel
  fields = ["city", "country", "description", "date"]

class TravelDelete(DeleteView):
  model = Travel
  success_url = "/travels/"

def add_activity(request, travel_id):
  form = ActivityForm(request.POST)