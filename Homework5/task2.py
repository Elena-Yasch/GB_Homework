# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open('hw5.txt', 'r', encoding='utf-8') as f_obj:
    text = f_obj.readlines()
    print(text)
    for i, line in enumerate(text, 1):
        num = len(line.split())
        print("Колличество слов в строке:", num)