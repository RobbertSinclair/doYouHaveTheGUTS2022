from backend_app.views import *
from django.contrib import admin
from django.urls import path

app_name = "backend_app"
urlpatterns = [
    path("", index, name="index"),
    path("event/", event, name="event"),
    path("profile/", profile, name="profile"),
    path("team/", team, name="team"),
    path("create-event/", create_event, name="create-event"),
]