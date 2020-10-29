import random


class Dog:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name}: Woff!")

    def make_trick(self):
        tricks = ['roll', 'sit', 'jump']
        print(f"{self.name}: making trick {random.choice(tricks)}")


class Cat:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name}: Mjau!")

    def make_trick(self):
        print(f"{self.name}: Cat's don't make tricks on demand!")



class Parrot:
    def __init__(self,name):
        self.name = name

    def make_sound(self):
        print(f"{self.name}: Kwak!")

    def make_trick(self):
        tricks = [f"Mitt namn är {self.name}!","making trik prituet.","Sitting down like buddha.",f"Sitting down like {Dog('Rufus').name}."]
        print(f"{self.name}: {random.choice(tricks)} Kwak!")


def play_with_animals():
    hund = Dog("Rufus")
    hund.make_sound()
    hund.make_trick()
    cat = Cat("Cecilia")
    cat.make_sound()
    cat.make_trick()
    parrot = Parrot("Max")
    parrot.make_sound()
    parrot.make_trick()


if __name__ == '__main__':
    play_with_animals()