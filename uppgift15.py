
#text=input("Ange en text,så ser vi hur många ord det är :")
#text = str(text).strip()
#text = text.split()
#counter= len(text)
#print(counter)
#print(type(text))

def vokal_count(char):

    if char.lower()== 'a' or char.lower()== 'e' or char.lower()== 'i' or char.lower()== 'u' or char.lower()== 'o' or char.lower()== 'y':
        #print(char)
        return True



def main():

    counter = 0
    text = input("ange en text")
    for char in text :
        if vokal_count(char):
            counter = counter +1
            print(char,counter)



if __name__ == '__main__':
   main()

