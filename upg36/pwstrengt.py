def compute_strength(pw):
    count = 0
    legit = '#%&+_-'



    if len(pw) > 10:
        count += 1

    if any(char.isalpha() for char in pw):
        if any(char.isalpha() for char in pw):
            count += 1

    if any(char in legit for char in pw):
             count += 1

    if any( not char.isalnum() and char not in legit for char in pw):
        count = 0
        print("Ogiltligt")

    return count