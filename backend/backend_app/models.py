from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import random

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
    revealed_date = models.DateField(default=None)
    revealed_time = models.TimeField(default=None)
    budget = models.DecimalField(max_digits=6, decimal_places=2)
    details = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    address = models.CharField(max_length=200)
    dietary_info = models.CharField(max_length=500)
    likes_and_dislikes = models.ManyToManyField(DietTag)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    profile_picture = models.ImageField(upload_to='profile_images', blank=True)
    team = models.CharField(max_length=50, default="NOTEAM")
    google_search_address = models.CharField(max_length=400, blank=True, null=True)
    partner_found = models.BooleanField(blank=True, null=True, default=False)
    buying_for = models.ForeignKey("self", related_name="partner", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        the_address = self.address
        the_address = the_address.replace(" ", "+")
        self.google_search_address = the_address

        super(UserProfile, self).save(self, *args, **kwargs)




class EventUserBridge(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user', null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default=None)
    opt_in = models.BooleanField()
    theme_opt_in = models.BooleanField()

    def __str__(self):
        return self.user.username
