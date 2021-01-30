from functools import reduce
import os as myos


my_list = [n for n in range(100, 1001, 1) if n % 2 == 0]

sum_all = reduce(lambda x, y: x * y, my_list)

print(sum_all)
