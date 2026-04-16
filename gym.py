gym_data = {
    "Brock": {
        "city": "Pewter City",
        "leader_team": [
            {"name": "geodude", "types": ["rock", "ground"], "level": 12},
            {"name": "onix", "types": ["rock", "ground"], "level": 14}
        ],
        "level_cap": 14,
        "available_ids": list(range(1, 22)) + [25, 29, 32, 56, 161] 
        # Routes 1, 2, 22, Viridian Forest
    },
    "Misty": {
        "city": "Cerulean City",
        "leader_team": [
            {"name": "staryu", "types": ["water"], "level": 18},
            {"name": "starmie", "types": ["water", "psychic"], "level": 21}
        ],
        "level_cap": 21,
        "available_ids": list(range(1, 57)) + [129]
        # Adds Mt. Moon, Routes 4, 24, 25, and Magikarp (Old Rod)
    },
    "Lt. Surge": {
        "city": "Vermilion City",
        "leader_team": [
            {"name": "voltorb", "types": ["electric"], "level": 21},
            {"name": "pikachu", "types": ["electric"], "level": 18},
            {"name": "raichu", "types": ["electric"], "level": 24}
        ],
        "level_cap": 24,
        "available_ids": list(range(1, 63)) + [50, 51, 96, 97]
        # Adds Route 5, 6, 11, S.S. Anne, and Diglett's Cave
    },
    "Erika": {
        "city": "Celadon City",
        "leader_team": [
            {"name": "victreebel", "types": ["grass", "poison"], "level": 29},
            {"name": "tangela", "types": ["grass"], "level": 24},
            {"name": "vileplume", "types": ["grass", "poison"], "level": 29}
        ],
        "level_cap": 29,
        "available_ids": list(range(1, 71)) + [83, 123, 127, 133]
        # Adds Routes 7, 8, 9, 10, Rock Tunnel, and Celadon City (Eevee/Game Corner)
    },
    "Koga": {
        "city": "Fuchsia City",
        "leader_team": [
            {"name": "koffing", "types": ["poison"], "level": 37},
            {"name": "muk", "types": ["poison"], "level": 39},
            {"name": "koffing", "types": ["poison"], "level": 37},
            {"name": "weezing", "types": ["poison"], "level": 43}
        ],
        "level_cap": 43,
        "available_ids": list(range(1, 110)) + [122, 128, 147]
        # Adds Route 12-18, Safari Zone, and Good Rod encounters
    },
    "Sabrina": {
        "city": "Saffron City",
        "leader_team": [
            {"name": "kadabra", "types": ["psychic"], "level": 38},
            {"name": "mr-mime", "types": ["psychic"], "level": 37},
            {"name": "venomoth", "types": ["bug", "poison"], "level": 38},
            {"name": "alakazam", "types": ["psychic"], "level": 43}
        ],
        "level_cap": 43,
        "available_ids": list(range(1, 122)) + [106, 107]
        # Adds Saffron City (Hitmons) and Silph Co.
    },
    "Blaine": {
        "city": "Cinnabar Island",
        "leader_team": [
            {"name": "growlithe", "types": ["fire"], "level": 42},
            {"name": "ponyta", "types": ["fire"], "level": 40},
            {"name": "rapidash", "types": ["fire"], "level": 42},
            {"name": "arcanine", "types": ["fire"], "level": 47}
        ],
        "level_cap": 47,
        "available_ids": list(range(1, 143)) + [144]
        # Adds Seafoam Islands and Pokemon Mansion
    },
    "Giovanni": {
        "city": "Viridian City",
        "leader_team": [
            {"name": "rhyhorn", "types": ["ground", "rock"], "level": 45},
            {"name": "dugtrio", "types": ["ground"], "level": 42},
            {"name": "nidoqueen", "types": ["poison", "ground"], "level": 44},
            {"name": "nidoking", "types": ["poison", "ground"], "level": 45},
            {"name": "rhyhorn", "types": ["ground", "rock"], "level": 50}
        ],
        "level_cap": 50,
        "available_ids": list(range(1, 151))
        # All Pokemon available before the Elite Four
    }
}