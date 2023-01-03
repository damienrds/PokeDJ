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
