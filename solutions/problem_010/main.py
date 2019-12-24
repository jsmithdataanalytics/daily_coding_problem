import time


def schedule_job(f, delay):
    time.sleep(0.001 * delay)

    return f()


if __name__ == '__main__':
    schedule_job(lambda: print('Success!'), 3000)
