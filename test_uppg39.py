from uppg39 import max,num_sum,num_prod

def test_max_return_biggest_value_if_a():
    a,b,c = 5,2,3
    assert max(a,b,c) == a

def test_max_return_biggest_value_if_b():
    a,b,c = 1,4,3
    assert max(a,b,c) == b

def test_max_return_biggest_value_if_c():
    a,b,c = 1,2,3
    assert max(a,b,c) == c

def test_num_sum():
    lista = [1,2,3,4,5]
    assert num_sum(lista) == sum(lista)

def test_num_prod():
    lista = [1,2,3,4,5,6]
    assert num_prod(lista) == 720