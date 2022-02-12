from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from backend_app.models import *
from backend_app.forms import EventForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, "index.html")

def event(request):
    return render(request, "event.html")

def team(request):
    context_dict = {}

    #event = Event.objects.get(slug=event_name_slug)
    # Gets all the members associated with that team
   # members = UserProfile.objects.filter(event=event)

    return render(request, "team.html", context=context_dict)



def sign_up(request):
    pass

def user_login(request):
    pass

def user_logout(request):
    pass

def my_account(request):
    return render(request, 'my_account.html')



@login_required
def create_event(request):
    form = EventForm()

    if request.method == 'POST':
        form = EventForm(request.POST,request.FILES)
        u = request.user
        user = UserProfile.objects.get(user_id=u.id)

        if form.is_valid():
            event = form.save(commit=False)
            return redirect(reverse('ratemyrecipeapp:index'))

        else:
            print(form.errors)
    
    context_dict = {} 
    context_dict['form']=form

    return render(request, "create_event.html", context=context_dict)