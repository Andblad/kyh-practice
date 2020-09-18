from conversions import m_to_mm, cm_to_m, mm_to_m, farenhite_to_cellsius


def test_conversion_from_meters_to_mm():
    expected = 1000
    got = m_to_mm(1)
    expected1 =  5000
    got1 = m_to_mm(5)

    assert(expected == got)
    assert  expected1 == got1


def test_cm_to_m():
    expected = 2
    got = cm_to_m(200)
    assert(expected == got)

def test_mm_to_m():
    expected = 1
    got = mm_to_m(1000)
    expected1 = 5
    got1 = mm_to_m(5000)

    assert (expected == got)
    assert expected1 == got1

def test_farenhite_to_cellsius():
    expected = -10
    got = farenhite_to_cellsius(14)
    expected1 = 0
    got1 = farenhite_to_cellsius(32)
    expected2 = 10
    got2 = farenhite_to_cellsius(50)

    assert expected == got
    assert expected1 == got1
    assert expected2 == got2






