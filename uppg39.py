def max(a,b,c):
    biggest = a
    if biggest < b:
        biggest = b
    if biggest < c:
        biggest = c
    return biggest

def num_sum(lista):
    sum_list = 0
    for num in lista:
        sum_list += num
    return sum_list

def num_prod(lista):
    sum_list = 1
    for num in lista:
        sum_list *= num
    return sum_list

def main():
    a = 1
    b = 2
    c = 3

    print(max(a,b,c))
    print(num_sum([a,b,c]))
    print(num_prod([1,2,3,4,5]))

if __name__ == '__main__':
    main()