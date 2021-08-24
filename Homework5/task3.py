# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
# средней величины дохода сотрудников.
with open('hw5-3.txt', 'r', encoding='utf-8') as f_obj:
    employees_dict = [item.replace('\n', '') for item in f_obj.readlines()]
    new_list = [employee.split()[0] for employee in employees_dict if int(employee.split()[1]) < 20000]
    print(new_list)
