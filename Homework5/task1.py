# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
with open ('my_doc.txt', 'w', encoding='utf-8') as my_doc:
    str_list = input('Как Вас зовут и сколько вам лет?')
    my_doc.writelines(str_list)
