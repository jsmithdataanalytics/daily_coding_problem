import json


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __eq__(self, other):
        return other and self.value == other.value and self.left == other.left and self.right == other.right

    @staticmethod
    def from_dict(dictionary):

        if not dictionary:
            return None

        node = Node(dictionary['value'])
        node.left, node.right = Node.from_dict(dictionary['left']), Node.from_dict(dictionary['right'])

        return node


def serialize(root):
    return json.dumps(root, default=lambda node: node.__dict__)


def deserialize(string):
    return Node.from_dict(json.loads(string))


if __name__ == '__main__':
    tree = Node('a')
    tree.left, tree.right = Node('b'), Node('c')
    tree.left.right = Node('d')

    assert deserialize(serialize(tree)) == tree
