
def cons(a, b):
    return lambda f: f(a, b)


def car(pair):
    return pair(lambda a, b: a)


def cdr(pair):
    return pair(lambda a, b: b)


if __name__ == '__main__':
    assert car(cons(3, 4)) == 3
    assert cdr(cons(3, 4)) == 4
