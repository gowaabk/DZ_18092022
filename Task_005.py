# Задайте список из k чисел последовательности (1 + 1 \ k) ^ k и выведите на экран их сумму


k = int(input('Введите k --> '))
print(sum((1 + 1 / i) ** i for i in range(1, k + 1)))