people = {
'Fredrik':'0702778511',
'Olof': '123456789',
'Lisa': '9999999999',
'Bodil': '555-666-789'
}




def main():
    hända = input("1:Slå upp nummer.\n2:Redigera lista.\nVad vill du göra:")
    if hända == '1':
        #print(F"Det finns {len(people)} personer i telefonlistan")
        vem = input('Vem vill du ringa?')
        if vem not in people:
            print('Sorry hörru, vet ej vem detta är. Har endast VIP i min katalog')
        else:
            number = people[vem]
            print(f"Numret till {vem} är {number}")
    if hända == '2':
        redi = input("Vill du:\n 1:Lägga till.\n2: Ta bort")
        if redi == '1':
             
        if redi == '2':

if __name__ == '__main__':
    main()