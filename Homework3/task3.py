# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

num_1 = int(input('Введите первое число - '))
num_2 = int(input('Введите второе число - '))
num_3 = int(input('Введите третье число - '))
new_list = []


def my_func(num_1, num_2, num_3):
    new_list = [num_1, num_2, num_3]
    new_list.sort()
    return new_list[-1] + new_list[-2]


print(my_func(num_1, num_2, num_3))
