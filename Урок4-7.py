import math
import itertools


def fact(end_number):
    s = 1
    for el in range(1, end_number):
        s = s*el
        yield s


for el in fact(9):
    print(el)
