# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в
# новый текстовый файл.
with open('hw5-4.txt', 'r', encoding='utf-8') as my_file:
    my_text = [item.replace('\n', '') for item in my_file.readlines()]
    new_list = [item.replace('One', 'Один').replace('Two', 'Два').replace('Three', 'Три').replace('Four', 'Четыре') for item in my_text]
    print(new_list)

with open('text.txt', 'w', encoding='utf-8') as new_file:
    new_file.writelines(new_list)