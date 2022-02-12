from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from backend_app.models import *
from backend_app.forms import EventForm

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

@login_required
def create_event(request):
        # Gets the recipe form from forms.py
    form = RecipeForm()

    if request.method == 'POST':
        form = RecipeForm(request.POST,request.FILES)
        u=request.user
        user=UserProfile.objects.get(user_id=u.id)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.added_by=user
            recipe.category = Cuisine.objects.get(slug=category_name_slug)
            recipe.save()
            return redirect(reverse('ratemyrecipeapp:index'))

        else:
            print(form.errors)
    
    context_dict = {} 
    context_dict['form']=form
    context_dict['category']=Category.objects.get(slug=category_name_slug)

    return render(request, 'ratemyrecipeapp/add_recipe.html', context=context_dict)
    return render(request, "create_event.html")