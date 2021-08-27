from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .models import Superhero
from django.urls import reverse

# Create your views here.
def index(request):
    all_heroes = Superhero.objects.all()
    context = {
        'all_heroes':  all_heroes
    }
    return render(request, 'superheros/index.html', context)

def detail(request, hero_id ):
    single_hero = Superhero.objects.get(pk = hero_id)
    context = { 
        'single_hero': single_hero
    }
    return render (request, 'superheros/detail.html', context)

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary = request.POST.get('primary')
        secondary = request.POST.get('secondary')
        catchpharase = request.POST.get('catchpharase')
        new_hero = Superhero(name=name, alter_ego = alter_ego, primary_ablity = primary, secondary_ablity = secondary, catch_phrase = catchpharase)
        new_hero.save()
        return HttpResponseRedirect (reverse('superheros:index'))
    else:
        return render (request, 'superheros/create.html')