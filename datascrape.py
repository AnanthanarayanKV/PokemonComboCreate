import csv 
import requests

def getDex(id):
    api = f"https://pokeapi.co/api/v2/pokemon/{id}"
    res = requests.get(api)

    if res.status_code == 200:
        data = res.json()

        stats = {
            "name": data["name"],
            "types": [t["type"]["name"] for t in data["types"]],
            "hp": data["stats"][0]["base_stat"],
            "attack": data["stats"][1]["base_stat"],
            "defence": data["stats"][2]["base_stat"],
            "special-attack": data["stats"][3]["base_stat"],
            "special-defence": data["stats"][4]["base_stat"],
            "speed": data["stats"][5]["base_stat"],

        }
        return stats
    else:
        print("Error data could not be fetched")
        return None

if __name__ == "__main__":
    header_names = ["name","types","hp","attack","defence","special-attack","special-defence","speed"]

    with open("pokedex.csv", mode = "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header_names)
        writer.writeheader()

        for i in range(1,152):
            pokemon_info = getDex(i)
            if pokemon_info:
                writer.writerow(pokemon_info)
                print(f"Fetched: {pokemon_info['name']}")


