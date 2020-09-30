import json
from pathlib import Path
p = Path('phonelists.json')
content = p.read_text(encoding='utf8')
data = json.loads(content)
people = data


def main():
    print('Det finns %s nummer i kattalogen' % (len(people)))
    hända = input("1:Slå upp nummer.\n2:Redigera lista.\nVad vill du göra:")
    if hända == '1':
        vem = input('Vem vill du ringa?')
        if vem not in people:
            print('Sorry hörru, vet ej vem detta är. Har endast VIP i min katalog')
        else:
            number = people[vem]
            print("Numret till %s är %s" % (vem,number))
    if hända == '2':
        redi = input("Vill du:\n 1:Lägga till/ Skriva över.\n2: Ta bort")
        if redi == '1':
            name = input("Skriv namn:")
            numb = input ("Ange nummer:")
            people[name] = numb
            c = json.dumps(people, indent=2  )

            p.write_text(f"{c}", encoding='utf8')
            print(people)

        if redi == '2':
            tabort = input("Vem vill du ta bort:")
            del people[tabort]
            print(people)

if __name__ == '__main__':
    main()