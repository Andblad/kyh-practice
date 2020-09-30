def info_tupel(t):
    print(f"Namn: {t[0]}")
    print(f"Ålder: {t[1]}")

def rev_tupel(t):
    return t[::-1]

def ls_till_tupel(t):
    return tuple(t)

info_tupel(('Tobias', 27))

print(rev_tupel((1,2,3,4)))

print(ls_till_tupel([1,2,3,'hesjan','haha']))