from programs.list_of_squares import list_of_squares

def test_list_of_squares_zero():

    assert list_of_squares(0) == {}

def test_list_of_squares_one():
    assert list_of_squares(2) == {1: 1, 2: 4}


def test_list_of_squares_many():
    assert list_of_squares(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


