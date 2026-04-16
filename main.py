import pandas as pd
import requests

def get_pokemon_data(name_or_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{name_or_id}"
    res = requests.get(url)
    if res.status_code != 200: 
        return None
    
    data = res.json()
    
    # Get unique level-up moves for FireRed/LeafGreen
    moves = {
        m["move"]["name"]
        for m in data["moves"]
        for version in m["version_group_details"]
        if version["version_group"]["name"] == "firered-leafgreen"
        and version["move_learn_method"]["name"] == "level-up"
    }

    # Flatten the data for a clean CSV row
    return {
        "id": data["id"],
        "name": data["name"],
        "types": ", ".join([t["type"]["name"] for t in data["types"]]),
        "moves": ", ".join(list(moves)),
        # Spread stats into individual columns
        **{s["stat"]["name"]: s["base_stat"] for s in data["stats"]}
    }

# 1. Collect all data in a list first
pokemon_list = []
print("Fetching Pokémon data...")

for i in range(1, 152):  # 151 is Mew
    pokemon = get_pokemon_data(i)
    if pokemon:
        pokemon_list.append(pokemon)

# 2. Create the DataFrame once
df = pd.DataFrame(pokemon_list)

# 3. Save to CSV once
df.to_csv("pokemon_firered_data.csv", index=False)
print("Done! Data saved to pokemon_firered_data.csv")