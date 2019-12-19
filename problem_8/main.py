
class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __eq__(self, other):
        assert self.value == other.value

    def __repr__(self):
        return f'Node(value={self.value.__repr__()}, left={self.left.__repr__()}, right={self.right.__repr__()})'

    def walk(self, callback):
        callback(self)

        if self.left:
            self.left.walk(callback)

        if self.right:
            self.right.walk(callback)

    def is_unival(self):

        try:
            self.walk(lambda node: node == self)

        except AssertionError:
            return 0

        return 1

    def count_unival_subtrees(self):
        unival_subtrees = []
        self.walk(lambda node: unival_subtrees.append(node.is_unival()))

        return sum(unival_subtrees)


if __name__ == '__main__':
    root = Node(0)
    root.left, root.right = Node(1), Node(0)
    root.right.left, root.right.right = Node(1), Node(0)
    root.right.left.left, root.right.left.right = Node(1), Node(1)

    assert root.count_unival_subtrees() == 5
