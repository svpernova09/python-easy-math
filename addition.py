#!/usr/bin/env python
# __author__ = "Joe Ferguson"
# __copyright__ = "Copyright 2019, Joe Ferguson"
# __credits__ = ["Joe Ferguson"]
# __maintainer__ = "Joe Ferguson"
# __email__ = "joe@joeferguson.me"


def add(x, y):
    """
    Addes x to y
    :param x: integer
    :param y: integer
    :return: value of x + y
    """
    return x + y


def subtract(x, y):
    """
    Subtracts y from x
    :param x: integer
    :param y: integer
    :return: value of x - y
    """
    return x - y


def main():  # pragma: no cover
    import argparse

    parser = argparse.ArgumentParser(
        description='Python library for calculating the sum of two numbers')
    # required parameters
    required = parser.add_argument_group('required arguments')
    required.add_argument('-x', '--x', dest='first', type=float, required=True, help='First Number')
    required.add_argument('-y', '--y', dest='second', type=float, required=True, help='Second Number')

    arguments = parser.parse_args()
    total = add(arguments.first, arguments.second)
    print("Total: {:,.2f}".format(total))


if __name__ == '__main__':  # pragma: no cover
    main()
