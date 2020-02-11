
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

cache = {'': ['']}


def decode(string):

    if string in cache:
        return cache[string]

    solutions = []

    for number, letter in enumerate(letters):
        number = str(number + 1)

        if len(string) >= len(number) and string[:len(number)] == number:

            for solution in decode(string[len(number):]):
                solutions.append(letter + solution)

    cache[string] = solutions

    return solutions


def count(string):
    return len(decode(string))


if __name__ == '__main__':
    assert count('111') == 3
