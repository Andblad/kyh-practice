from pathlib import Path
import json
p = Path('data.json')
content= p.read_text(encoding='utf8')

data=json.loads(content)
print(data)



