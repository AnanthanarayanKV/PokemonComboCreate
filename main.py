import requests

def get_Pokemon(pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}"

    response = requests.get(url)

    if response.status_code ==200:
        data = response.json()

        specs = {
            "name": data["name"],
            "type": [t["type"]["name"] for t in data["types"]],
            "b_stats": {s["stat"]["name"]: s["base_stat"] for s in data["stats"]},
            "speed": data["stats"][5]["base_stat"]
        }
        return specs
    else:
        return "Error: Pokemon not found"
    

print(get_Pokemon("Charizard"))