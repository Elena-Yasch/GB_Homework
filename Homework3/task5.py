# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных
# пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ
# введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме
# и после этого завершить программу.
def get_sum():

    result = 0
    stop_symbol = '*'
    while True:
        numbers = input('Введите числа через пробел.\nДля остановки введите звездочку.')

        if numbers == '*':
            break
        elif numbers.split()[-1] == stop_symbol:
            numbers_list = numbers.split()[:-1]
            numbers_list_int = map(int, numbers_list)
            result += sum(numbers_list_int)
            print(result)

            break

        numbers_list = numbers.split()
        numbers_list_int = map(int, numbers_list)

        result += sum(numbers_list_int)
        print(result)

get_sum()

