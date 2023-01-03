import pokepy

def get_pokemon_info(iPokemonName):
    vClient = pokepy.V2Client()
    vPokemonInfo = {}
    
    vPokemon = vClient.get_pokemon(iPokemonName)[0]
    vPokemonInfo[vPokemon.name] = {
        "id": vPokemon.id,
        "name": vPokemon.name,
        "type": [vPokemon.types[index_type].type.name for index_type in range(len(vPokemon.types))],
        "ability": [vPokemon.abilities[index_ability].ability.name for index_ability in range(len(vPokemon.abilities))],
        "sprite": vPokemon.sprites.front_default,
        "height": vPokemon.height,
        "weight": vPokemon.weight,
        "stats": {
            "PV": vPokemon.stats[0].base_stat,
            "Attaque": vPokemon.stats[1].base_stat,
            "Defense": vPokemon.stats[2].base_stat,
            "AttaqueSpe": vPokemon.stats[3].base_stat,
            "DefenseSpe": vPokemon.stats[4].base_stat,
            "Vitesse": vPokemon.stats[5].base_stat
        }
    }
        
    return vPokemonInfo
