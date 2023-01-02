from django.http import HttpResponse
from django.shortcuts import render
import pokepy
from PokeDJ.util.pokedex_1G import pokedex_1G

def index(request):
    vPokedex = pokedex_1G()
    vContext = {
        "pokedex":vPokedex,
    }
    return render(request, "pokedex_home.html", context=vContext)
