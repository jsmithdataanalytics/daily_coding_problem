
def products(ints):
    answer = []
    forward, backward = [], []
    forward_cumulative_product = backward_cumulative_product = 1

    for i in range(len(ints)):
        forward_cumulative_product *= ints[i]
        forward.append(forward_cumulative_product)
        backward_cumulative_product *= ints[-(i + 1)]
        backward = [backward_cumulative_product] + backward

    for i in range(len(ints)):
        forward_part = forward[i - 1] if i else 1
        backward_part = backward[i + 1] if i + 1 <= len(ints) - 1 else 1
        answer.append(forward_part * backward_part)

    return answer


if __name__ == '__main__':
    assert products([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert products([3, 2, 1]) == [2, 3, 6]
