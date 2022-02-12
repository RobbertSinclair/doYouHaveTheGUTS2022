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


def generate_event_test():
    from datetime import datetime

    event_name = "Valentine's Lunch"
    event = Event.objects.get_or_create(name=event_name)[0]
    event.date = datetime.strptime('2-14-22', '%m-%d-%y')
    event.time = datetime.strptime("12:30", "%H:%M")
    event.budget = 10.00
    event.details = "Lunch dates, cheeky."
    event.save()

def event(request):
    #generate_event_test()
    context_dict = {}
    next_event = "Valentines"
    try:
        cur_event = Event.objects.get(name=next_event)
        context_dict['event'] = cur_event
    except Event.DoesNotExist:
        context_dict['event'] = None

    return render(request, "event.html", context=context_dict)


def profile(request):
    return render(request, "profile.html")

def team(request):
    context_dict = {}
    return render(request, "team.html", context=context_dict)


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