import json
from pathlib import Path
from pprint import pprint

p = Path('uppgift27.json')
fil = p.read_text()

#print(f"{fil['what']}")

#pprint([len(fil)])
for elem in fil:
    print(f"{elem['what'],elem['value']},{elem['unit']}")