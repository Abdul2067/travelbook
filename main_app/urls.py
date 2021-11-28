from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
  path("", views.Home.as_view(), name="home"),
  path("about/", views.about, name="about"),
  path("travels/", views.travels_index, name="travels_index"),
  path("travels/<int:travel_id>/", views.travels_detail, name="travels_detail")
]
