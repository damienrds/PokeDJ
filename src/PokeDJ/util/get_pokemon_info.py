import pokepy

def get_pokemon_info(iPokemonName):
    vClient = pokepy.V2Client()
    vPokemonInfo = {}
    
    vPokemon = vClient.get_pokemon(iPokemonName)[0]
    vPokemonInfo = {
        "id": vPokemon.id,
        "name": vPokemon.name,
        "type": [vPokemon.types[index_type].type.name for index_type in range(len(vPokemon.types))],
        "ability": [vPokemon.abilities[index_ability].ability.name for index_ability in range(len(vPokemon.abilities))],
        "sprite": vPokemon.sprites.front_default,
        "height": int(vPokemon.height)/10,
        "weight": int(vPokemon.weight)/10,
        "stats": {
            "PV": vPokemon.stats[0].base_stat,
            "Attaque": vPokemon.stats[1].base_stat,
            "Defense": vPokemon.stats[2].base_stat,
            "AttaqueSpe": vPokemon.stats[3].base_stat,
            "DefenseSpe": vPokemon.stats[4].base_stat,
            "Vitesse": vPokemon.stats[5].base_stat
        },
        "moves": [],
    }
    
    # -- Fill movepool --------------------------------------------------------
    for index_move in range(len(vPokemon.moves)):
        vMove = vClient.get_move(vPokemon.moves[index_move].move.url.split("/")[-2])[0]
        vPokemonInfo["moves"].append({
            "name": vMove.name,
            "type": vMove.type.name,
            "power": vMove.power,
            "accuracy": vMove.accuracy,
            "pp": vMove.pp,
            "damage_class": vMove.damage_class.name,
        })
    
    return vPokemonInfo