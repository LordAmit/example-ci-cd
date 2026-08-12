from calc.arithmetic import add


def test_adding_two_positives():
    assert add(2, 3) == 5


def test_adding_zero_changes_nothing():
    assert add(7, 0) == 7


def test_adding_a_negative():
    assert add(2, -3) == -1
