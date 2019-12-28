
INTERVALS = 1000

pi = 0

for i in range(-INTERVALS, INTERVALS):
    (x_min, x_max) = (i / INTERVALS, (i + 1) / INTERVALS)

    for j in range(-INTERVALS, INTERVALS):
        (y_min, y_max) = (j / INTERVALS, (j + 1) / INTERVALS)
        (centre_x, centre_y) = ((x_min + x_max) / 2, (y_min + y_max) / 2)

        if centre_x ** 2 + centre_y ** 2 < 1:
            pi += INTERVALS ** (-2)

assert round(pi, 3) == 3.142
