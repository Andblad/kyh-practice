import random
antal_gissngar = 0
n = random.randint(1, 100)
print("Jag tänker på ett tal mellan 1 och 100, vilket?")

while True:
    text = input("Din gissning: ")
    as_number = int(text)

    if as_number == n:
        print("Korekt!")
        antal_gissngar =antal_gissngar +1
        break

    if as_number < n:
        print("Fel, mitt tal är högre... Testa igen!")

    if as_number > n:
        print("Fel, mitt tal är lägre... testa igen!")
    antal_gissngar = antal_gissngar +1
print("Du gissade" , antal_gissngar ,"antal gånger.")