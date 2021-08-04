#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите
# в формате чч:мм:сс. Используйте форматирование строк.
time_sec = int(input('Enter a time in seconds:'))
time_hour = time_sec // 3600
time_min = time_sec % 3600
time_min_1 = time_min // 60
time_sec_1 = time_sec % 60
print(f'Your time - {time_hour:02}:{time_min_1:02}:{time_sec_1:02}')
