import pokepy

def pokedex_1G():
    vClient = pokepy.V2Client()
    vPokedex_1G = {}
    
    for index in range(1, 152):
        vPokemon = vClient.get_pokemon(index)[0]
        vPokedex_1G[vPokemon.name] = {
            "id": vPokemon.id,
            "name": vPokemon.name,
            "type": [vPokemon.types[index_type].type.name for index_type in range(len(vPokemon.types))],
            "ability": [vPokemon.abilities[index_ability].ability.name for index_ability in range(len(vPokemon.abilities))],
            "sprite": vPokemon.sprites.front_default,
        }
        
    return vPokedex_1G

pokedex_1G()