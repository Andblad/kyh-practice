FRUITS = ['banana', 'apple', 'orange']
CARS = ['volvo', 'ford', 'tesla']
ANIMALS = ['cat','dog','wolf','worm']

def run():
    basket = input("Add items to sort in lists:").split(',')

    cars = []
    fruits = []
    rest = []
    animal = []
    for item in basket:
        if item in CARS:
            cars.append(item)
        elif item in FRUITS:
            fruits.append(item)
        elif item in ANIMALS:
            animal.append(item)
        else:
            rest.append(item)
    write_things(cars, 'Cars')
    write_things(fruits, 'Fruits')
    write_things(animal, 'Animals')
    write_things(rest, 'Misc')


def write_things(items, kind):
    print(f"{kind.upper()} ({len(items)}st)")
    items = sorted(items)
    for item in items:
        print(f" {item}")


if __name__ == '__main__':
    run()