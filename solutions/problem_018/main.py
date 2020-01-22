from collections import deque


def print_subarray_maxes(array, k):
    queue = deque()

    for i in range(k):

        while queue and array[i] > queue[-1]:
            queue.pop()

        queue.append(array[i])

    print(queue[0])

    for i in range(1, len(array) - k + 1):

        if queue[0] == array[i - 1]:
            queue.popleft()

        while queue and array[i + k - 1] > queue[-1]:
            queue.pop()

        queue.append(array[i + k - 1])

        print(queue[0])


if __name__ == '__main__':
    print_subarray_maxes([10, 5, 2, 7, 8, 7], 3)
