# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
with open('num_file.txt', 'w', encoding='utf-8') as new_file:
    num_list = ['1 2 3 4 5 6 7 8 9']
    new_file.writelines(num_list)

with open('num_file.txt', 'r', encoding='utf-8') as new_2file:
    num = new_2file.readlines()[0]
    new_2list = [int(elm) for elm in num.split()]
    print(sum(new_2list))
