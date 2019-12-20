
class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def build(self, ints):

        while ints and ints[0] <= 0:
            ints.pop(0)

        if not ints:
            return self.value

        self.left = Node(self.value + ints[0])
        left_answer = right_answer = self.left.build(ints[2:])

        if len(ints) > 1 and ints[1] > 0:
            self.right = Node(self.value + ints[1])
            right_answer = self.right.build(ints[3:])

        return max(left_answer, right_answer)


def greatest_sum_of_non_consecutive_integers(ints):
    return Node(0).build(ints)


if __name__ == '__main__':
    assert greatest_sum_of_non_consecutive_integers([2, 4, 6, 8]) == 12
    assert greatest_sum_of_non_consecutive_integers([5, 1, 1, 5]) == 10
    assert greatest_sum_of_non_consecutive_integers([-1, -5, 4, 9, -3, 1, 0, 8]) == 18
