import wget
import json

FILE = "files.json"

with open(FILE) as f:
    data = json.load(f)
    for mod in data["mods"]:
        if mod["client"]: continue
        name = mod["name"]
        desc = mod["description"]
        print(f"{name}: {desc}")
    
