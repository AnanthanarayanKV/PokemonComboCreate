import pandas as pd
from mechanics import damage_calculator
from gym import gym_data

def find_ultimate_counter(gym_name):
    gym = gym_data[gym_name]
    cap = gym["level_cap"] # This is 14 for Brock
    
    df = pd.read_csv('pokemon_data.csv')
    df.columns = df.columns.str.strip().str.lower()
    df['id'] = df['id'].astype(int)
    
    available_df = df[df['id'].isin(gym['available_ids'])].copy()
    all_results = []

    for _, row in available_df.iterrows():
        p_id = row['id']

        # --- NEW: EVOLUTION FILTER ---
        # If the level cap is low (like Brock), we remove Pokemon that 
        # haven't evolved yet.
        if cap < 16:
            # IDs of Mid/Final stage Pokemon available early
            # 2: Ivysaur, 3: Venusaur, 5: Charmeleon, 6: Charizard, 
            # 8: Wartortle, 9: Blastoise, 11: Metapod, 12: Butterfree...
            invalid_early = [2, 3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18, 22]
            if p_id in invalid_early:
                continue
        
        elif cap < 32:
            # For Misty/Surge, we allow Mid-stages (Ivysaur) but not Finals (Venusaur)
            invalid_mid = [3, 6, 9]
            if p_id in invalid_mid:
                continue
        # -----------------------------

        score = 0
        raw_types = row['types']
        my_types = [t.strip() for t in raw_types.split(',')] if isinstance(raw_types, str) else [raw_types]
        
        for leader_pkmn in gym["leader_team"]:
            target_types = leader_pkmn["types"]
            for my_t in my_types:
                score += (damage_calculator(my_t, target_types) * 10)
            for enemy_t in target_types:
                score -= (damage_calculator(enemy_t, my_types) * 5)

        all_results.append({
            "name": row['name'],
            "score": score,
            "types": raw_types
        })

    sorted_team = sorted(all_results, key=lambda x: x['score'], reverse=True)
    return sorted_team[:6]

out = pd.DataFrame(find_ultimate_counter("Brock"))
print(out)