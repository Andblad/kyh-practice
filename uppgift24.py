import json
import datetime
import requests
from pprint import pprint
dag = datetime.datetime.today()
URL = 'https://proagile.se/api/publicEvents'
r = requests.get(URL)

text = r.text
list = json.loads(text)
#print(str(dag.date()))
y = input("Ange år:")
m = input("Ange månad:")
startdate= f"{y}-{m}-01"
enddate = f"{y}-{m}-31"
#print(date)
for element in list:
        if element['startDate'] >= startdate and element['startDate'] <= enddate :
                 print(f"Krusnamn:    {element['name']}\nStartdatum: {element['startDate']:>11}\nSlutdatum:{element['endDate']:>13}")





