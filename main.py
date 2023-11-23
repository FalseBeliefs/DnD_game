import json

with open("sword.json", "r") as file:
    data = json.load(file)

print(data)
Max_HP = data["player"]["maxHealth"]
Current_HP = data["player"]["currentHealth"]
Weapon_name = data["player"]["mainHandWeapon"]["name"]

print(f"HP: {Current_HP}/{Max_HP}")
print(f"Main hand: {Weapon_name}")

this is new