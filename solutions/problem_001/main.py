
def is_sum_possible(numbers, target):
    target = float(target)
    required = set()

    for number in numbers:
        number = float(number)

        if number in required:
            return True

        required.add(target - number)

    return False


if __name__ == '__main__':
    assert is_sum_possible([10, 15, 3, 7], 17)
