from upp40 import versal,minMAX,bak

def test_bak():
    assert bak('abc123') == '321cba'

def test_bak_blank():
    assert  bak('') == ''

def test_bak_with_space():
    assert bak("abc def") == "fed cba"

def test_versal():
    assert versal("AbCdE") == 3