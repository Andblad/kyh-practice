def bak(skrift):
    str = ''
    for i in skrift:
        str = i + str
    return str

def versal(text):
    count = 0
    for l in text:
        if l == l.upper():
            count += 1
    return count

def minMAX(value,min,max):
    if value < min:
        return False
    if value > max:
        return False
    else:
        return True

if __name__ == '__main__':
    a = 'AjaBAka'
    #print(versal(a))
    print(bak(a))
    #print(minMAX(value=10,min=1,max=100))