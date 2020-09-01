import random
antal_gissngar = 0
n = random.randint(1, 100)
print("Jag tänker på ett tal mellan 1 och 100, vilket?")

while True:
    text = input("Din gissning: ")
    as_number = int(text)
    antal_gissngar = antal_gissngar + 1
    if as_number == n:
        print("Korekt!")

        break

    if as_number < n:
        print("Fel, mitt tal är högre... Testa igen!")

    if as_number > n:
        print("Fel, mitt tal är lägre... testa igen!")

print("Du gissade" , antal_gissngar ,"antal gånger.")