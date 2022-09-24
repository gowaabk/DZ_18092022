# Найти сумму чисел списка стоящих на нечетной позиции


import random


def create_random_list(list2: list, width: int):  # Функция генерации списка
    for i in range(width):
        list2.append(random.randint(0, width))
    return list2


my_list = []
my_list = create_random_list(my_list, 8)
sum_odd = sum(my_list[item] for item in range(1, len(my_list), 2))
odd_el = [my_list[item] for item in range(1, len(my_list), 2)]
print(
    f'Для списка {my_list} сумма чисел, стоящих на нечётных позициях: \n{odd_el} равна {sum_odd}.')
