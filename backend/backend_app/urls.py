from backend_app.views import *
from django.contrib import admin
from django.urls import path

app_name = "backend_app"
urlpatterns = [
    path("", index, name="index"),
    path("event/", event, name="event"),
    path("team/", team, name="team"),
    path("create-event/", create_event, name="create-event"),
    path("restaurants/<str:keyword>", restaurants, name="restaurants"),

    path('signUp/', sign_up, name="signUp"),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name='logout'),
    path('account/', my_account, name="account"),
    path("my_account", my_account, name="my_account"),
]