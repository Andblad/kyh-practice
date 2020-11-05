from upg36.pwstrengt import compute_strength

def test_password_length_11_gives_1_point():
    pw = '1' * 11
    assert compute_strength(pw) == 1

def test_password_alpanumeric_gives_1_point():
    pw = 'abc123'
    assert compute_strength(pw) == 1

def test_password_sign_gives_1_point():
    pw = '#%&'
    assert compute_strength(pw) == 1

def test_password_othersign_0_point():
    pw = '()!'
    assert compute_strength(pw) == 0

def test_password_lenght_and_alphanumeric_2_point():
    pw = 'ac1' * 6
    assert compute_strength(pw) == 2

def test_password_lenght_and_alphanumeric_sign_3_point():
    pw = 'ac1#' * 6
    assert compute_strength(pw) == 3

