from random import randint


def create_example_stream(n):
    i = 0

    while i < n:
        i += 1

        yield i


def sample(stream):
    i, answer = 0, None

    for obj in stream:
        i += 1

        if randint(1, i) == i:
            answer = obj

    return answer


if __name__ == '__main__':
    print(sample(create_example_stream(1000000000)))
