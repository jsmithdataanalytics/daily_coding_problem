
def lowest_missing_integer(ints):
    i, length = 0, len(ints)

    while i < length:
        advance, destination = True, ints[i] - 1

        if 1 <= ints[i] <= length and ints[i] != ints[destination]:
            ints[i], ints[destination] = ints[destination], ints[i]

            if destination > i:
                advance = False

        if advance:
            i += 1

    for i, num in enumerate(ints):

        if num != i + 1:
            return i + 1

    return length + 1


if __name__ == '__main__':
    assert lowest_missing_integer([3, 4, -1, 1]) == 2
    assert lowest_missing_integer([1, 2, 0]) == 3
