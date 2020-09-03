import random

def game(antal,max):
    correct_answers = 0



    for i in range(antal):

        a = random.randint(1, max)
        b = random.randint(1, max)

        while True:
            answer = input(f"{a}+{b}")

            try:
                number = int(answer)
                break

            except ValueError:
                   print("Ej heltal inmatat, försök igen.")

        if number == a + b:
            print("Rätt!")
            correct_answers += 1

        else:
            print(f"Fel... Det blir {a+b}")
            print("---")

    print(f"Du fick {correct_answers} av {antal} rätt.")

if __name__ == '__main__':


    antal = int(input("Ange antal tal som du vill räkna på: "))


    max = int(input("Ange största talet som skall andvändas:"))



    game(antal,max)