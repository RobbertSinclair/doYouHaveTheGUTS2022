from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from backend_app.models import *
from backend_app.forms import *
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponse
from backend_app.forms import *
import requests
import json

# Create your views here.
def index(request):
    data = requests.get(f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=55.871914%2C-4.297744&radius=2500&type=restaurant&keyword=cruise&key={settings.GOOGLE_KEY}")
    print(data.json())
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
    # To test create a Valentines model in admin page
    next_event = "Valentines"
    current_user = request.user
    print(current_user)
    try:
        cur_event = Event.objects.get(name=next_event)
        context_dict['event'] = cur_event
    except Event.DoesNotExist:
        context_dict['event'] = None

    if context_dict['event'] != None:
        try:
            options = EventUserBridge.objects.get(user=current_user)
            print(options)
            context_dict['options'] = options
        except:
            context_dict['options'] = None

    print(context_dict["options"])

    return render(request, "event.html", context=context_dict)


def team(request):
    context_dict = {}

    event = Event.objects.get(name="Jimmy's Birthday")
    members = UserProfile.objects.filter(event=event)

    context_dict["event"] = event
    context_dict["members"] = members
    return render(request, "team.html", context=context_dict)



def sign_up(request):
    # Is registration successful?
    registered = False

    if request.method == 'POST':
        # Attempt to grab info from raw form information
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save user's form data to database
            user = user_form.save()

            # Set then update password
            user.set_password(user.password)
            user.save()

            # Set commit=False to delay saving model
            # until ready to avoid integrity problems
            profile = profile_form.save(commit=False)
            profile.user = user

            # Saves UserProfile instance
            profile.save()

            # Update variable to indicate to template registration was successful
            registered = True
        else:
            # Invalid form(s)
            # Prints problems to terminal
            print(user_form.errors, profile_form.errors)
    else:
        # Not an HTTP POST so form rendered using two ModelForm instances
        # These forms will be blank, ready for user input
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render template depending on context
    return render(request,
                  'sign_up.html',
                  context={'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})


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
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        u = request.user
        user = UserProfile.objects.get(user_id=u.id)

        if event_form.is_valid():
            event = event_form.save(commit=False)
            return redirect(reverse('backend_app:index'))

        else:
            print(event_form.errors)
    else:
        # If not a HTTP POST then render a blank form.
        event_form = EventForm()
    
    return render(request, 'create_event.html', {'event_form': event_form})