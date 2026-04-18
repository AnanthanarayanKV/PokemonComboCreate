from pathlib import Path
import csv
from datascrape import getDex

file = Path("pokedex.csv")

# 1. Ensure the file exists before moving forward
if not file.exists():
    print("File not found. Fetching data now...")
    getDex()
    print("Download complete.")

# 2. Now that we are certain it exists (or was just created), proceed
if file.exists():
    print("Data gathered and available. Starting program...")

player_Pokemon = []
for i in range(0,3):
    poke = input(f"Enter pokemon no:{i+1} :>")
    poke = poke.lower()
    player_Pokemon.append(poke)


with open("pokedex.csv","r",newline='') as file:
    read = csv.DictReader(file)
    i = 0;
    for row in read:
        if row["name"] in player_Pokemon:
            print(row)