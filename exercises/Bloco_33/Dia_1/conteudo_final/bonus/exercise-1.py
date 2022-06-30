import sys


def lowest_number(arr):
    winner_number = sys.maxsize
    for x in arr:
        if x < winner_number:
            winner_number = x
    return winner_number


print(lowest_number([5, 9, 3, 19, 70, 8, 100, 2, 35, 27]))
