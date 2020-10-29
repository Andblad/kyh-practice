def age_sorter(pepole):
    pass


anna = ("Anna","Person",32)
lova = ("Lova","Börjeson",45)
alex = ("Alex","Anders",10 )
pepole = [anna,lova,alex]
on_age = []
hig_age = None
for p in pepole:
    if hig_age == None:
        on_age.append(p)
    if p[2] < hig_age:
        on_age.append(p)
    if p[2] > hig_age:
        on_age[0] = p

