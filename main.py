""" Monte Carlo Pi Estimation """
import random
import math

def getPointInCircle():
    """calculate whether a point would be in a circle"""
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
    return 1 if (x**2 + y**2) <= 1 else 0

def main():
    """ Main driver, estimate pi 2 ways """
    sample_size = 10000000
    points_in_circle = 0
    for _ in range(sample_size):
        points_in_circle += getPointInCircle()

    print(math.pi)
    print(round(4.0 * points_in_circle / sample_size, 3))

    points_in_circle = 0
    tries = 0
    while True:
        tries += 1
        points_in_circle += getPointInCircle()
        if points_in_circle >= sample_size:
            print(round(4.0 * points_in_circle / tries, 3))
            break


if __name__ == "__main__":
    main()
