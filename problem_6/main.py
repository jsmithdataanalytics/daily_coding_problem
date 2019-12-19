
pointers = {}


def get_pointer(obj):
    return obj.pointer


def dereference_pointer(pointer):
    return pointers[pointer]


class Node:

    def __init__(self, value):
        self.value = value
        self.both = 0

        self.pointer = len(pointers) + 1
        pointers[self.pointer] = self


class LinkedList(Node):

    def __iter__(self):
        return LinkedListIter(self)

    @property
    def tail(self):
        tail = None

        for node in self:
            tail = node

        return tail

    def get_node(self, index):

        assert isinstance(index, int)
        assert index >= 0

        for node in self:

            if not index:
                return node

            index -= 1

        raise IndexError()

    def get(self, index):
        return self.get_node(index).value

    def add(self, value):
        new = Node(value)
        tail = self.tail
        tail.both = tail.both ^ get_pointer(new)
        new.both = get_pointer(tail)


class LinkedListIter:

    def __init__(self, head):
        self.head = head
        self.current = None
        self.previous = None

    def __next__(self):

        if self.current is None:
            self.current = self.head

            return self.current

        previous_pointer = get_pointer(self.previous) if self.previous is not None else 0

        if self.current.both == 0 or previous_pointer == self.current.both:
            raise StopIteration()

        self.previous, self.current = self.current, dereference_pointer(self.current.both ^ previous_pointer)

        return self.current


if __name__ == '__main__':
    linked_list = LinkedList(5)
    linked_list.add(4)
    linked_list.add(3)
    linked_list.add(2)

    for element in linked_list:
        print(element.value)

    assert linked_list.get(0) == 5
    assert linked_list.get(1) == 4
    assert linked_list.get(2) == 3
    assert linked_list.get(3) == 2

    try:
        linked_list.get(4)

        raise Exception()

    except IndexError:
        print('Success!')
