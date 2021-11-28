from django.http import request
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
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
  success_url = "/travels/"

