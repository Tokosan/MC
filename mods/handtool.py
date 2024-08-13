import wget
import json

FILE = "../admin/files.json"

with open(FILE) as f:
    data = json.load(f)
    for mod in data["mods"]:
        url = mod["url"]
        # descargamos los mods
        wget.download(url)
    for lib in data["libraries"]:
        url = lib["url"]
        # descargamos las librerias
        wget.download(url)
    
