people = {
'Fredrik':'0702778511',
'Olof': '123456789',
'Lisa': '9999999999',
'Bodil': '555-666-789'
}




def main():
    hända = input("1:Slå upp nummer.\n2:Redigera lista.\nVad vill du göra:")
    if hända == '1':
        #print(f"Det finns {len(people)} personer i telefonlistan")# Skriver ut antla personer i listan.
        vem = input('Vem vill du ringa?')
        if vem not in people:
            print('Sorry hörru, vet ej vem detta är. Har endast VIP i min katalog')
        else:
            number = people[vem]
            print(f"Numret till {vem} är {number}")
    if hända == '2':
        redi = input("Vill du:\n 1:Lägga till/ Skriva över.\n2: Ta bort")
        if redi == '1':
            name = input("Skriv namn:")
            numb = input ("Ange nummer:")
            people[name] = numb
            print(people)
        if redi == '2':
            tabort = input("Vem vill du ta bort:")
            del people[tabort]
            print(people)

if __name__ == '__main__':
    main()