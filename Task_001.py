# Дана последовательность чисел.
# Получить список уникальных элементов заданной последовательности.

import random


def create_random_list(list2: list, width: int):  # Функция генерации списка
    for i in range(width):
        list2.append(random.randint(0, width))
    return list2


my_list = []
my_list = create_random_list(my_list, 8)
result_list = list(filter(lambda a: my_list.count(a) == 1, my_list))
print(
    f'Для списка {my_list}, \n   список уникальных элементов --> {result_list}')
