import wget
import json

FILE = "files.json"

with open(FILE) as f:
    data = json.load(f)
    # print("Descargando mods...")
    # for mod in data["mods"]:
    #     try:
    #         url = mod["url"]
    #         filename = wget.download(url)
    #     except:
    #         print(f"\nError downloading {mod["name"]}\n")

    # print("Descarga finalizada")
    
    print("Descargando librerias...")
    for lib in data["libraries"]:
        try:
            url = lib["url"]
            filename = wget.download(url)
        except:
            print(f"\nError downloading {lib["name"]}\n")
    
