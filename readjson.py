import json

with open('Playerdatabase.json') as file:
    data = json.load(file)
    print(data)
    for players in data["player_characters"]:
        char_id = players["id"]
        name = players["name"]

        print()
        print(f"{name}: {char_id}")
        print(f"{players["age"]},{players["class"]}")
        print(f"strenght:{players["strenght"]}, Dexterity {players["Dexterity"]}")
        print()
