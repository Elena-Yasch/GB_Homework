#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
num = int(input("Enter a positive integer:"))
num_max = 0
while num !=0:
    if num % 10 > num_max:
        num_max = num % 10
    num = num//10
print("The highest digit in the number:", num_max)
