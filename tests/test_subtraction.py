from calc.arithmetic import subtract


def test_subtracting_three_from_five():
    assert subtract(5, 3) == 2


def test_subtracting_a_number_from_itself():
    assert subtract(4, 4) == 0


def test_subtracting_a_negative():
    assert subtract(2, -3) == 5
