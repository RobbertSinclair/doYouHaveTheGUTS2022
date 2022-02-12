from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from backend_app.models import *
from backend_app.forms import EventForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponse

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
    # If request is HTTP POST, try to pull relevant info
    if request.method == 'POST':
        # Get username and password from login form
        username = request.POST.get('username')
        password = request.POST.get('password')

        # If username/password combination valid, User object is returned
        user = authenticate(username=username, password=password)

        # If we have as User object, the details are correct
        # If None, no user with matching credential found
        if user:
            # Is account active?
            if user.is_active:
                # If account valid and active, log user in and send back to homepage
                login(request, user)
                return redirect(reverse('backend_app:index'))
            else:
                # An inactive account was used so doesn't log in
                return HttpResponse("Your LunchBox account is disabled.")
        else:
            # Bad login details provided, so doesn't log in
            print("Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")

    # The request is not HTTP POST, so display login form
    # This would be HTTP GET
    else:
        # No context variables to pass to template system so blank dict. object
        return render(request, 'login.html')


@login_required
def user_logout(request):
    # Since we know user is logged in, we can just log them out
    logout(request)
    # Returns user to homepage
    return redirect(reverse('backend_app:index'))


def my_account(request):
    context_dict = {}
    u=request.user
    user=UserProfile.objects.get(user=u.id)
    context_dict["u"] = user
    return render(request, 'my_account.html', context=context_dict)



@login_required
def create_event(request):
    event_form = EventForm()
    
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        u = request.user
        user = UserProfile.objects.get(user_id=u.id)

        if event_form.is_valid():
            event = event_form.save(commit=False)
            return redirect(reverse('ratemyrecipeapp:index'))

        else:
            print(event_form.errors)
    
    context_dict = {} 
    context_dict['event_form'] = event_form

    return render(request, "create_event.html", context=context_dict)