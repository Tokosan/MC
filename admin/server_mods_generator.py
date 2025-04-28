import json
from urllib import parse

FILE = "files_v2.json"

with open(FILE) as f:
    data = json.load(f)
    output = ""
    for mod in data["mods"]:
        if not mod["server"]:
            continue

        url = mod["url"]
        filename = url.split("/")[-1]
        filename = parse.quote(filename)
        url = url.rsplit("/", 1)[0] + "/" + filename
        output += url + "\n"

    for mod in data["libraries"]:
        url = mod["url"]
        filename = url.split("/")[-1]
        filename = parse.quote(filename)
        url = url.rsplit("/", 1)[0] + "/" + filename
        output += url + "\n"
    # print(output)
    with open("mod-list.txt", "w") as f:
        f.write(output)
