import random

def game():
    correct_answers = 0



    for i in range(antal):

        a = random.randint(1, 10)
        b = random.randint(1, 10)
        answer = input(f"{a}+{b}")
        number = int(answer)

        if number == a + b:
            print("Rätt!")
            correct_answers += 1

        else:
            print(f"Fel... Det blir {a+b}")
            print("---")

    print(f"Du fick {correct_answers} av {antal} rätt.")

if __name__ == '__main__':
    antal = int(input("Ange antal tal som du vill räkna på: "))

    game()