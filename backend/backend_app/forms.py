from django import forms
from django.contrib.auth.models import User
from backend_app.models import Event, UserProfile

class EventForm(forms.ModelForm):
    name = forms.CharField(
        max_length=Event.NAME_MAX_LENGTH,
        help_text='Please enter the event name.'
    )

    date = forms.DateField()
    time = forms.TimeField()
    budget = forms.IntegerField()
    details = forms.CharField()
    #slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Event
        fields = ('name', 'date', 'time', 'budget', 'details')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', )


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ()
