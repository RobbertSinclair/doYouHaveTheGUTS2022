from django import forms
from django.contrib.auth.models import User
from backend_app.models import *

from django import forms

class CuisineForm(forms.ModelForm):
    name = forms.CharField(max_length=MAX_STRING_LENGTH)

    class Meta:
        model = Cuisine
        fields = ('name',)

class RestaurantForm(forms.ModelForm):
    name = forms.CharField(max_length=MAX_STRING_LENGTH)
    location = forms.CharField(max_length=200)
    image = forms.ImageField()

    class Meta:
        model = Restaurant
        exclude = ('cuisine',)
    
class MenuItemForm(forms.ModelForm):
    item = forms.CharField(max_length=MAX_STRING_LENGTH)
    price = forms.DecimalField(max_digits=6, decimal_places=2)
    image = forms.ImageField()

    class Meta:
        model = MenuItem
        exclude = ('restaurant',)


class DietTag(forms.ModelForm):
    name = forms.CharField(max_length=MAX_STRING_LENGTH)

    class Meta:
        model = DietTag
        fields = ('name',)

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class EventForm(forms.ModelForm):
    name = forms.CharField(max_length=MAX_STRING_LENGTH, widget=forms.TextInput(attrs={"class": "form-control"}))
    date = forms.DateField(widget=DateInput(attrs={"class": "form-control"}))
    time = forms.TimeField(widget=TimeInput(attrs={"class": "form-control"}))
    budget = forms.DecimalField(max_digits=6, decimal_places=2, widget=forms.NumberInput(attrs={"class": "form-control"}))
    details = forms.CharField(max_length=200, widget=forms.Textarea(attrs={"class": "form-control", "rows": 5, "cols": 20,}))

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