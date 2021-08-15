# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
# у пользователя, предусмотреть обработку ситуации деления на ноль.

num_1 = int(input('Введите первое число - '))
num_2 = int(input('Введите второе число - '))

def my_func(num_1, num_2):
    result = None
    try:
        result = num_1 / num_2
    except ZeroDivisionError:
        print("Делить на ноль нельзя!")

    return result

print(my_func(num_1, num_2))
