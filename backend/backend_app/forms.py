from django import forms
from django.contrib.auth.models import User
from backend_app.models import *

class CuisineForm(forms.ModelForm):
    name = forms.CharField(max_length=MAX_STRING_LENGTH)

    class Meta:
        model = Cuisine
        fields = ('name',)

class RestaurantForm(forms.ModelForm):
    name = forms.CharField(max_length=MAX_STRING_LENGTH)
    location = forms.CharField(max_length=200)
    image = forms.ImageField(help_text='Insert a Restaurant image here.')

    class Meta:
        model = Restaurant
        exclude = ('cuisine',)
    
class MenuItemForm(forms.ModelForm):
    item = forms.CharField(max_length=MAX_STRING_LENGTH)
    price = forms.DecimalField(max_digits=6, decimal_places=2)
    image = forms.ImageField(help_text='Insert a Menu Item image here.')

    class Meta:
        model = MenuItem
        exclude = ('restaurant',)


class DietTag(forms.ModelForm):
    name = forms.CharField(max_length=MAX_STRING_LENGTH)

    class Meta:
        model = DietTag
        fields = ('name',)

class EventForm(forms.ModelForm):
    name = forms.CharField(max_length=MAX_STRING_LENGTH, help_text='Please enter the category name.')
    date = forms.DateField()
    time = forms.TimeField()
    budget = forms.DecimalField(max_digits=6, decimal_places=2)
    details = forms.CharField(max_length=200)

    class Meta:
        model = Event
        fields = ('name', 'date', 'time', 'budget', 'details',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    address = forms.CharField(max_length=200)
    dietary_info = forms.CharField(max_length=500)
    profile_picture = forms.ImageField(help_text='Insert a User Profile Image here.')

    class Meta:
        model = UserProfile
        exclude = ('event',)