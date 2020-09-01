nummer = 0
total = 0
while True :
    print("För att avsluta, ange avslut")
    x = input ("Ange ett nummer:")
    if x == "avslut":
        break
    try:
        floatvar = float(x)
    except:
        print("ogiltlig input")
        continue
    nummer = nummer + 1
    total = total + floatvar
print("Här är total summan,antal input, och genomsnittet:")
print(total,nummer, total/nummer)