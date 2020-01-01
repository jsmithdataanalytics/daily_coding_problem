
class Queue(dict):

    def __init__(self, max_length):
        super().__init__(self)
        self.max_length = max_length
        self.first = 0
        self.last = -1

    def record(self, order_id):
        self.last += 1

        if len(self) == self.max_length:
            del self[self.first]
            self.first += 1

        self[self.last] = order_id

    def get_last(self, i):
        return self[self.last - i + 1]


if __name__ == '__main__':
    q = Queue(max_length=3)
    q.record('a')
    q.record('b')
    q.record('c')
    q.record('d')

    assert q.get_last(1) == 'd'
    assert q.get_last(2) == 'c'
    assert q.get_last(3) == 'b'

    try:
        q.get_last(4)

    except KeyError:
        print('Success!')
