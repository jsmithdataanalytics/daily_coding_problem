
def count_unique_climbs(num_stairs, valid_strides):
    num_climbs = 0

    for stride in valid_strides:

        if stride == num_stairs:
            num_climbs += 1

        if stride < num_stairs:
            num_climbs += count_unique_climbs(num_stairs - stride, valid_strides)

    return num_climbs


if __name__ == '__main__':
    assert count_unique_climbs(4, {1, 2}) == 5
    assert count_unique_climbs(6, {1, 3, 5}) == 8
