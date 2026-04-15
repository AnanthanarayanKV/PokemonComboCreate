import requests
import csv
import time
from mechanics import damage_calculator

def get_pokemon(id):
    url = f"https://pokeapi.co/api/v2/pokemon/{id}"

    response = requests.get(url)

    if response.status_code ==200:
        data = response.json()

        specs = {
            "name": data["name"],
            "type": [t["type"]["name"] for t in data["types"]],
            "hp": data["stats"][0]["base_stat"],
            "attack": data["stats"][1]["base_stat"],
            "defense": data["stats"][2]["base_stat"],
            "S_attack": data["stats"][3]["base_stat"],
            "S_defense": data["stats"][4]["base_stat"],
            "speed": data["stats"][5]["base_stat"]
        }
        return specs
    else:
        return "Error: Pokemon not found"
    

def get_and_save_pokemon(start, end):
    pokemons = []
    for i in range(start, end + 1):
        result = get_pokemon(i)
        if isinstance(result, dict): # Only add if it's a valid dictionary
            pokemons.append(result)
    
    if not pokemons:
        print("No data found.")
        return

    keys = pokemons[0].keys()

    with open('pokemon.csv','w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(pokemons)

    print("Pokemon.csv is created")

print(f"Fire vs Grass/Poison: {damage_calculator('fire', ['grass', 'poison'])}x")