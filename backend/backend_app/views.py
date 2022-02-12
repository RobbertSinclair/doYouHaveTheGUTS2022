from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def event(request):
    return render(request, "event.html")

def profile(request):
    return render(request, "profile.html")

def team(request):
    context_dict = {}
    return render(request, "team.html", context=context_dict)

def create_event(request):
    return render(request, "create.html")