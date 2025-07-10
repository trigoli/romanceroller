import json

with open('Playerdatabase.json') as file:
    data = json.load(file)
    players = data["player_characters"][0]
    print(players["name"])