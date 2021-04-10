import math


def demo(a, b, c) -> object:
    """
    :return:
    :param a:
    :param b:
    :param c:
    :return:
    """
    d = b ** 2 - 4 * a * c
    if d >= 0:
        disc = math.sqrt(d)
        root1 = (- b + disc) / (2 * a)
        root2 = (- b - disc) / (2 * a)
        print(root1, root2)
        return root1, root2
    else:
        raise Exception


class Solver(object):
    pass
