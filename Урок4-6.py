import itertools


def my_iter_f(start_number, end_number):
    for el in itertools.count(start_number):
        if el > end_number:
            break
        else:
            yield el


def my_iter_fcycle(objekt_cycle, end_number):
    с = 1
    for el in itertools.cycle(objekt_cycle):
        if с > end_number:
            break
        else:
            с += 1
            yield el


def my_print_iter(my_iter):
    try:
        print(next(my_iter))
    except StopIteration:
        print('End list')


# my_iter = itertools.count(start=0, step=1)
my_iter = []
my_iter = my_iter_f(3, 12)

n = 1
while n < 13:
    n = n + 1
    my_print_iter(my_iter)

p_value = ["python", "java", "perl"]
m_list = my_iter_fcycle(p_value, 10)

n = 0
while n < 12:
    n = n + 1
    my_print_iter(m_list)
