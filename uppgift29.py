import requests
import webbrowser
from pathlib import Path
r = requests.get('https://api.adviceslip.com/advice')
advice = r.json()
dict = advice['slip']
value = dict['advice']


content = Path('uppgift29.html').read_text()
html = content.replace('QUOTE_TEXT', value)
#print(html)
p = Path('goat_q.html')
p.write_text(html, encoding='utf8')
#goat_q = fil.write('goat_quote.html')
webbrowser.open('goat_q.html')


