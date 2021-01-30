from sys import argv
import my_functions

if len(argv) != 5:
    print('Введено не достаточное количество параметров')
elif not argv[2].isnumeric():
    print('Введено не числовое значение вроботки')
elif not argv[3].isnumeric():
    print('Введено не числовое значение часов')
elif not argv[4].isnumeric():
    print('Введено не числовое значение размера процента премии')
else:
    zp = my_functions.z_calculate(int(argv[2]), int(argv[3]), int(argv[4]))
    print(f'Сотрудник {argv[1]}, заработал сумму {zp}')
