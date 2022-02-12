from django import forms
from django.contrib.auth.models import User
from backend_app.models import *
#from backend_app.models import

class EventForm(forms.ModelForm):
    name = forms.CharField(
        max_length=30,
        help_text='Please enter the category name.'
    )
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    picture = forms.ImageField(
        help_text='Insert a category image here.'
    )

    class Meta:
        model = Cuisine
        fields = ('name', 'picture', )
