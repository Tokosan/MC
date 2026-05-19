import json

FILE = "files_v2.json"

with open(FILE) as f:
    data = json.load(f)
    for mod in data["mods"]:
        name = mod["name"]
        description = mod["description"]
        print(f"[{name}]({mod['curseforge']}): {description}")
