from easy_math import addition


def test_add_amount():
    data = [
        [0, 0, 0],
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 2],
        [1337, 1337, 2674],
        [2500, 4700, 7200],
    ]

    for i, val in enumerate(data):
        assert addition.add(val[0], val[1]) == val[2]

