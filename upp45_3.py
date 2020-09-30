import json
from pathlib import Path
from pprint import pprint

p = Path('uppgift27.json')
text = p.read_text(encoding='utf8')
fil = json.loads(text)


for elem in fil:
    if elem['rightalign'] == True:
        print("{:>25}{:>12}{}".format(elem['what'],elem['value'],elem['unit']))
    else:
        print("%-25s %12s %s" % (elem['what'],elem['value'],elem['unit']))