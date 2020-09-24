from upg36 import pwstrengt
pw = input("Ange lösenord\n>> ")
print(f"Ditt lösernord fick {pwstrengt.compute_strength(pw)} poäng av 3 mjöliga.")