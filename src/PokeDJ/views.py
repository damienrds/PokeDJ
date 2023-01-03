from django.http import HttpResponse
from django.shortcuts import render
import pokepy
from PokeDJ.util.pokedex import pokedex

def index(request):
    vPokedex_1G = pokedex(1, 151)
    vContext = {
        "pokedex_1G":vPokedex_1G,
    }
    return render(request, "pokedex_home.html", context=vContext)

def view_gen(request, generation):
    
    if generation == 1:
        vPokedex = pokedex(1, 151)
        vRegion = "Kanto"
    elif generation == 2:
        vPokedex = pokedex(152, 251)
        vRegion = "Johto"
    elif generation == 3:
        vPokedex = pokedex(252, 386)
        vRegion = "Hoenn"
    elif generation == 4:
        vPokedex = pokedex(387, 493)
        vRegion = "Sinnoh"
    elif generation == 5:
        vPokedex = pokedex(494, 649)
        vRegion = "Unova"
    elif generation == 6:
        vPokedex = pokedex(650, 721)
        vRegion = "Kalos"
    elif generation == 7:
        vPokedex = pokedex(722, 809)
        vRegion = "Alola"
    elif generation == 8:
        vPokedex = pokedex(810, 898)
        vRegion = "Galar"
    else:
        vPokedex = {}
        vRegion = "Unknown"
    
    vContext = {
        "pokedex":vPokedex,
        "generation":generation,
        "region":vRegion,
    }
    return render(request, "pokedex_gen.html", context=vContext)

