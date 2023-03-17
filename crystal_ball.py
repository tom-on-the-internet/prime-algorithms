import math


def crystal_ball(breaks_on, top):
    turns = 0

    i = 1
    while True:
        turns += 1
        height = math.isqrt(top) * i
        if height >= breaks_on:
            i -= 1
            break
        i += 1

    print(turns)

    j = 0
    while True:
        turns += 1
        height = math.isqrt(top) * i + j
        print(height)
        if height >= breaks_on:
            return turns
        j += 1


if __name__ == "__main__":
    print(crystal_ball(3923, 10000))
