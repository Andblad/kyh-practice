import json

import requests
from pprint import pprint

URL = 'https://proagile.se/api/publicEvents'
r = requests.get(URL)

text = r.text
list = json.loads(text)

for element in list:
        print(element['startDate'])





