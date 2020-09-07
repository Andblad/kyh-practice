def is_it_too_long(name, antal):

    return len(name) > antal

def main(antal):


    students=input("Ange studenters namn med , imellan:").split(",")

    #students = ["anna", "beatrice", "cecilia", "doris", "esmeralda", "frida", "gunilla"]
    for name in students:

        if is_it_too_long(name,antal):
            print(f"{name.capitalize()} är för långt!")

if __name__ == '__main__':

    try:
        antal = int(input("Ange antal bokstäver som maxlängd för namn: "))
    except ValueError:
        print("Heltal ej anget. Sätter antal bokstäver till 5.")
        antal=5
    main(antal)