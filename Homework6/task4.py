# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police(булево). А также методы: go, stop, turn(), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    speed = ''
    color = ''
    name = ''
    is_police = False

    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed

    def go(self):
        print('Машина поехала!')

    def stop(self):
        print('Машина остановилась!')

    def turn(self, direction):
        print('Машина повернула - ', direction)

    def show_speed(self):
        print(f'Машина {self.name}, цвет: {self.color}, едет со скоростью - {self.speed} км.')


class TownCar(Car):

    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)

    def show_speed(self):
        print(f'Машина {self.name}, цвет: {self.color}, едет со скоростью -  {self.speed} км.')
        if self.speed >= 60:
            print('ПРЕВЫШЕНИЕ СКОРОСТИ!\n')


class SportCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)


class WorkCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)

    def show_speed(self):
        print(f'Машина {self.name}, цвет: {self.color}, едет со скоростью -  {self.speed} км.')
        if self.speed >= 40:
            print('ПРЕВЫШЕНИЕ СКОРОСТИ!\n')


class PoliceCar(Car):
    is_police = True

    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)


car_1 = TownCar('KIA RIO', 'Белый', 63)
car_1.show_speed()
car_2 = SportCar('Porsche Cayene', 'Черный', 110)
car_2.show_speed()
car_3 = WorkCar('YAZ', 'Серый', 45)
car_3.show_speed()
car_4 = PoliceCar('Toyota Corolla', 'Белый с синими полосами', 80)
car_4.show_speed()