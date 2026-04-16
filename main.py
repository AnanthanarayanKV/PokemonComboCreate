import requests
import requests
import pandas as pd
from mechanics import damage_calculator
from gym import gym_data

def get_pokemon_data(name_or_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{name_or_id}"
    res = requests.get(url)
    if res.status_code != 200: return None
    data = res.json()
    
    moves = []
    for m in data["moves"]:
        for version in m["version_group_details"]:
            if version["version_group"]["name"] == "firered-leafgreen":
                if version["move_learn_method"]["name"] == "level-up":
                    moves.append(m["move"]["name"])

    return {
        "id": data["id"],
        "name": data["name"],
        "types": [t["type"]["name"] for t in data["types"]],
        "moves": list(set(moves)),
        "stats": {s["stat"]["name"]: s["base_stat"] for s in data["stats"]}
    }

def recommend_team(gym_name):
    gym = gym_data[gym_name]
    leader_pokemon = [get_pokemon_data(p) for p in gym["leader_team"]]
    
    recommendations = []
    
    print(f"Analyzing counters available for {gym_name}...")
    
    for p_id in gym["available_ids"]:
        candidate = get_pokemon_data(p_id)
        if not candidate: continue
        
        score = 0
        for p in leader_pokemon:
            for l_type in p["types"]:
                score -= damage_calculator(l_type, candidate["types"])
            
            for c_type in candidate["types"]:
                score += (damage_calculator(c_type, p["types"]) * 2)
        
        recommendations.append({"name": candidate["name"], "score": score})

    # Sort and show top 5
    top_5 = sorted(recommendations, key=lambda x: x['score'], reverse=True)[:10]
    
    print(f"\n--- Top 5 Recommended for {gym_name} ---")
    for i, rec in enumerate(top_5, 1):
        print(f"{i}. {rec['name'].capitalize()} (Score: {rec['score']})")

# Run the tool 
recommend_team("Brock")