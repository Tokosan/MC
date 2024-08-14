import wget
import json

FILE = "files.json"

with open(FILE) as f:
    data = json.load(f)
    for mod in data["mods"]:
        if mod["client"]: continue
        name = mod["name"]
        description = mod["description"]
        print(f"[{name}]({mod['curseforge']}): {description}")
        
    # for mod in data["mods"]:
    #     url = mod["url"]
    #     # descargamos los mods
    #     wget.download(url)
    # for lib in data["libraries"]:
    #     url = lib["url"]
    #     # descargamos las librerias
    #     wget.download(url)
