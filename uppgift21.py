from pathlib import Path
import json

p = Path('massasdata.json').read_text()

data = json.loads(p)
total_lists = []

for item in data['entries']:
    total_lists.append(item['total'])

print(sum(total_lists))

