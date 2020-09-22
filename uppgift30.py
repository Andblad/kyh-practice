from pprint import pprint
#regnum = input("Ange reg nummer:")
#print(f"Bokstäver: {regnum[0:3]}")
#print(f"Siffror: {regnum[3:]}")

num =input("Ange ettt antal tal, skilj vid komma: ").split(",")
print(f"Första talet: {num[0]}\nSista talet: {num[-1]}")
summa = []
for elem in num:
    summa.append(int(elem))
print(f"Summan av talen: {sum(summa)}")
#rNum = ' '.join([str(item)for item in num])
print(f"Talen baklänges: {' '.join(num[::-1])}")
num.reverse()
print(f"Talen baklänges: {' '.join(num)}")