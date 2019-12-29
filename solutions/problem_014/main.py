from random import uniform

ITERATIONS = 100000000

hits = 0

for _ in range(ITERATIONS):
    random_point = (uniform(-1, 1), uniform(-1, 1))

    if random_point[0] ** 2 + random_point[1] ** 2 < 1:
        hits += 1

pi = hits / ITERATIONS * 4


if __name__ == '__main__':
    assert round(pi, 3) == 3.142
