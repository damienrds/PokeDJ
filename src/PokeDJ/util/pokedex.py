import pokepy

def pokedex(iStart, iEnd):
    vClient = pokepy.V2Client()
    vPokedex_1G = {}
    
    for index in range(iStart, iEnd + 1):
        vPokemon = vClient.get_pokemon(index)[0]
        vPokedex_1G[vPokemon.name] = {
            "id": vPokemon.id,
            "name": vPokemon.name,
            "type": [vPokemon.types[index_type].type.name for index_type in range(len(vPokemon.types))],
            "sprite": vPokemon.sprites.front_default,
            "stats": {
                "PV": vPokemon.stats[0].base_stat,
                "Attaque": vPokemon.stats[1].base_stat,
                "Defense": vPokemon.stats[2].base_stat,
                "AttaqueSpe": vPokemon.stats[3].base_stat,
                "DefenseSpe": vPokemon.stats[4].base_stat,
                "Vitesse": vPokemon.stats[5].base_stat
        },

        }
        
    return vPokedex_1G