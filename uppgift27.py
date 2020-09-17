import json
from pathlib import Path
from pprint import pprint

p = Path('uppgift27.json')
text = p.read_text(encoding='utf8')
fil = json.loads(text)
#print(f"{fil['what']}")

#pprint([len(fil)])

for elem in fil:
    if elem['rightalign'] == True:
        print(f"{elem['what']:>25}{elem['value']:>12}{elem['unit']}")
    else:
        print(f"{elem['what']:<25}{elem['value']:>12}{elem['unit']}")