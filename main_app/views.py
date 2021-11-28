from django.http import request
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from . models import Travel

# Create your views here.

class Home(LoginView):
  template_name = "home.html"

def about(request):
  return render(request, "about.html")

def travels_index(request):
  travels = Travel.objects.all()
  return render(request, "travels/index.html", {"travels" : travels})