import webbrowser
from pathlib import Path

OUTPUT_PATH = Path("djur.html")
TEMPLATE_PATH = Path('djur_template.html')

# DEFINIERA CLASS Djur!
class Djur:
    def __init__(self, name, carnivore, wiki_url):
        self.name = name
        self.carnivore = carnivore
        self.wiki_url = wiki_url

    def carnivore_or_vegetarian(self):
        if self.carnivore:
            return "Köttätare"
        else:
            return "Vetegarian"

    def get_html_tabel_row(self):
        html =  f'<tr><td><a href="{self.wiki_url}">{self.name}</td><td>{d.carnivore_or_vegetarian()}</td></tr>\n'
        return html

if __name__ == '__main__':
    djur = []
    zebra = Djur('Zebra', False, 'https://sv.wikipedia.org/wiki/Zebror')
    tiger = Djur('Tiger', True, 'https://sv.wikipedia.org/wiki/Tiger')
    panda = Djur('Panda', False,'https://sv.wikipedia.org/wiki/J%C3%A4ttepanda')
    pingvin = Djur('Pingvin',True,'https://sv.wikipedia.org/wiki/Pingviner')
    sjöhäst = Djur('Sjöhäst',True,'https://sv.wikipedia.org/wiki/Sj%C3%B6h%C3%A4star')
    djur.append(zebra)
    djur.append(tiger)
    djur.append(panda)
    djur.append(pingvin)
    djur.append(sjöhäst)

    html = '<html><table>'
    for d in djur:
        html += d.get_html_tabel_row()
    html += '</table></html>'
    OUTPUT_PATH.write_text(html, encoding='utf8')
    webbrowser.open(str(OUTPUT_PATH))