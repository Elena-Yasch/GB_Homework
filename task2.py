#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите
# в формате чч:мм:сс. Используйте форматирование строк.
user_sec = int(input('Enter the time in seconds:'))
time_hour = user_sec // 3600
time_min = (user_sec % 3600) // 60
time_sec = user_sec % 60
print(f'Your time - {time_hour:02}:{time_min:02}:{time_sec:02}')
