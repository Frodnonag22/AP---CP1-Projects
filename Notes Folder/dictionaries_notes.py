# AP, Dictionaries Notes

# Collection of Key and Value pairs

kar = { # Key: Value,
    "make": "Jeep",
    "model": "Wrangler",
    "color": "silver",
    "year": 2023
}

values = list(kar.values())

print(values)
print(len(kar))
if "transmission" in kar:
    print(kar["transmission"])
else:
    kar["transmission"] = "automatic"

kar.pop("color")
print(kar.items())
keys = list(kar.keys())
for key in keys:
    print(f"{key} is {kar[key]}")



avatar = {
    "Water": {
        "Katara": "Water bender",
        "Sokka": "Leader. Boomerang guy. Idea guy. Sword master",
    },
    "Earth": {
        "Toph": "Earth bender",
        "Suki": "Warrior from Kyoshi Island",
        "Cabbage guy": "MY CABBAGES!!!!!!!!!"
    },
    "Air": {
        "Aang": "Air bender, the Avatar."
    },
    "Fire": {
        "Zuko": "Fire bender, future fire lord.",
        "Iroh": "The actual GOAT. Fire bender, Dragon of the West.",
        "Azula": "Fire lord for one hour. Amazing fire bender"
    }
}

print(avatar["Fire"]["Iroh"])
print(avatar.get("Earth").get("Cabbage guy"))