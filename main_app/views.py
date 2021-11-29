from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from . models import Travel
from .forms import ActivityForm

# Create your views here.

class Home(LoginView):
  template_name = "home.html"

def about(request):
  return render(request, "about.html")

@login_required
def travels_index(request):
  travels = Travel.objects.filter(user=request.user)
  return render(request, "travels/index.html", {"travels" : travels})

@login_required
def travels_detail(request, travel_id):
  travel = Travel.objects.get(id=travel_id)
  activity_form = ActivityForm()
  return render(request, "travels/detail.html", { "travel" : travel, "activity_form" : activity_form })

class TravelCreate(LoginRequiredMixin ,CreateView):
  model = Travel
  fields = ["city", "country", "description", "date"]

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class TravelUpdate(LoginRequiredMixin ,UpdateView):
  model = Travel
  fields = ["city", "country", "description", "date"]

class TravelDelete(LoginRequiredMixin ,DeleteView):
  model = Travel
  success_url = "/travels/"

@login_required
def add_activity(request, travel_id):
  form = ActivityForm(request.POST)
  if form.is_valid():
    new_activity = form.save(commit=False)
    new_activity.travel_id = travel_id
    new_activity.save()
  return redirect("travels_detail", travel_id=travel_id)

def signup(request):
  error_message = ""
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect("travels_index")
    else:
      error_message = "Invalid signup!! Please try again."
  form = UserCreationForm()
  context = {"form" : form, "error_message" : error_message}
  return render(request, "signup.html", context)