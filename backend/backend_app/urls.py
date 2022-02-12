from backend_app.views import *
from django.contrib import admin
from django.urls import path

app_name = "backend_app"
urlpatterns = [
    path("", index)
]