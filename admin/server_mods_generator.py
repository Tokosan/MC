import json
from urllib import parse

FILE = "files.json"

with open(FILE) as f:
    data = json.load(f)
    output = ""
    for download in data["mods"]:
        if not download["server"]: continue
        
        url = download['url']
        filename = url.split("/")[-1]
        filename = parse.quote(filename)
        url = url.rsplit("/", 1)[0] + '/' + filename
        output += url + "\n"
            
            
    for download in data["libraries"]:
        url = download['url']
        filename = url.split("/")[-1]
        filename = parse.quote(filename)
        url = url.rsplit("/", 1)[0] + '/' + filename
        output += url + "\n"
    # print(output)
    with open("mods.txt", "w") as f:
        f.write(output)
   
