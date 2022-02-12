from tkinter.tix import MAX
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

MAX_STRING_LENGTH = 128

class Cuisine(models.Model):
    name = models.CharField(max_length=MAX_STRING_LENGTH)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=MAX_STRING_LENGTH)
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='restaurant_images', blank=True)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    item = models.CharField(max_length=MAX_STRING_LENGTH)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu_item_images', blank=True)
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.item

class DietTag(models.Model):
    name = models.CharField(max_length=MAX_STRING_LENGTH)
    is_likes = models.BooleanField()

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=MAX_STRING_LENGTH)
    date = models.DateField()
    time = models.TimeField()
    budget = models.DecimalField(max_digits=6, decimal_places=2)
    details = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    address = models.CharField(max_length=200)
    dietary_info = models.CharField(max_length=500)
    likes_and_dislikes = models.ManyToManyField(DietTag)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_images', blank=True)
    team = models.CharField(max_length=50, default="NOTEAM")

    def __str__(self):
        return self.user.username


class EventUserBridge(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user', null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default=None)
    opt_in = models.BooleanField()
    theme_opt_in = models.BooleanField()

    def __str__(self):
        return self.user.username