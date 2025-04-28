import json

import wget

FILE = "../admin/files_v2.json"
PATH_FILES = "C:\\Users\\cteib\\Documents\\Personal\\Servers\\MC\\archivos\\"
PATH_LIBS = PATH_FILES + "librerias\\"
PATH_CLIENT = PATH_FILES + "necesarios\\"
PATH_EXTRAS = PATH_FILES + "opcionales\\"
PATH_TOOLS = PATH_FILES + "herramientas\\"


with open(FILE) as f:
    data = json.load(f)
    for mod in data["mods"]:
        url = mod["url"]
        # descargamos los mods
        if mod["client"]:
            wget.download(url, out=PATH_CLIENT)
        else:
            wget.download(url, out=PATH_EXTRAS)

    for lib in data["libraries"]:
        url = lib["url"]
        # descargamos las librerias
        wget.download(url, out=PATH_LIBS)

    for tool in data["tools"]:
        url = tool["url"]
        # descargamos las librerias
        wget.download(url, out=PATH_TOOLS)
