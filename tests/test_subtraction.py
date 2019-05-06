from easy_math import subtraction


def test_subtract_amount():
    data = [
        [0, 0, 0],
        [0, 1, -1],
        [1, 0, 1],
        [1, 1, 0],
        [2674, 1337, 1337],
    ]

    for i, val in enumerate(data):
        assert subtraction.subtract(val[0], val[1]) == val[2]

