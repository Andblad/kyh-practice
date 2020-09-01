import random

n = random.randint(1, 100)
print("Jag tänker på ett tal mellan 1 och 100, vilket?")

def ask_number():
    text = input("Din gissning: ")
    as_number = int(text)
    return as_number

def mainloop(n):


    while True:
        as_number = ask_number()
        if as_number == n:
         print("Korekt!")
         break

        if as_number < n:
            print("Fel, mitt tal är högre... Testa igen!")

        if as_number > n:
            print("Fel, mitt tal är lägre... testa igen!")
    return

mainloop(n)
