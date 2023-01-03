from django.http import HttpResponse
from django.shortcuts import render
import pokepy
from PokeDJ.util.pokedex import pokedex

def index(request):
    vPokedex = pokedex(1, 151)
    vContext = {
        "pokedex":vPokedex,
    }
    return render(request, "pokedex_home.html", context=vContext)
