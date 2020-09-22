num =input("Ange ettt antal tal, skilj vid komma: ").split(",")
print(f"Första talet: {num[0]}\nSista talet: {num[-1]}")
even = [i for i in num if int(i)%2==0]
#for i in list(num):
    #if (int(i)%2 == 0):
        #even.append(i)

odd = [i for i in num if int(i)%2==1]
#for i in list(num):
    #if (int(i)%2 == 1):
        #odd.append(i)
print(f"Jämna tal : {' '.join(even)}")
print(f"Ojämna tal: {' '.join(odd)}")
summa = [int(elem)for elem in num]
#eNum = [(elem%2) == 0 for elme in num ]
#print(f"Jämna tal : {eNum}")
print(f"Summan av talen: {sum(summa)}")

print(f"Talen baklänges: {' '.join(num[::-1])}")
num.reverse()
print(f"Talen baklänges: {' '.join(num)}")