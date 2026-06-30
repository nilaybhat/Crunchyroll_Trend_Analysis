from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("analysis/", views.dashboard, name="analysis"),
    path("prediction/", views.prediction, name="prediction"),
    path("team/", views.team, name="team"),
    path("contact/", views.contact, name="contact"),
]