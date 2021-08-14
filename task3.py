# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.
num = input('Enter any number:')
num_1 = num * 2
num_2 = num * 3
sum_num = int(num) + int(num_1) + int(num_2)
print('The sum of the numbers = ', sum_num)
