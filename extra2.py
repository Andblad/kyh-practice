char = input("Ange en bokstav, så ser vi om det är en vokla eller ej:")

while True:
    if (char == 'a' or char =='å' or char =='o'or char=='ö' or char == 'i' or char =='ä'or char =='u'or char =='y'or char =='e'):
        print("är vokal")
        break
    if (char == 'A' or char == 'Å' or char == 'O' or char == 'Ö' or char == 'I' or char == 'Ä' or char == 'U' or char == 'Y' or char == 'E'):
        print("är vokal")
        break
    else:
        print("är inte vokal")