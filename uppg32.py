text = input("Skriv nått: ")
#print(len(text))

text_revers = text[::-1]

print(text, text_revers)
text_rep = text.replace(' ','')
text_revers_rep = text_revers.replace(' ','')
print(text_rep)
if text_rep.lower() == text_revers_rep.lower():
    print("Detta är ett palindrom")
else:
    print("Detta är ej ett palidrom")




#b = a.replace(' ','')

#print(b)