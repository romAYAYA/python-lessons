# TODO ООП
import datetime
import time


# Объектно-ориентированное программирование: способ представления взаимодействий сущностей как в реальной жизни

# Процедурное программирование Паскаль
# Объектно-ориентированное программирование C#, Делфи, Python, C++
# Функциональное программирование F# Haskel

# Сущности:
# объект - видимость, рендеринг, коллизии (физики)
# техника - скорость, масса, может с ними взаимодействовать
# сухопутные водоплавающие - точки, где можно перемещаться
# Велосипед Машина Мотоцикл гидро скутер Лодка - текстуры, цвет

# TODO простой пример

# Наследование
# Полиморфизм
# Инкапсуляция
# Множественное наследование
class Mother1:  # Mother1(object)
    eyes = 'blue'


m1 = Mother1()  # инициализация класса (создание экземпляра)
print('цвет глаз матери:', m1.eyes)


class Child(Mother1):  # Наследование от класса Mother1
    age = 7
    eyes = 'green'  # override - переопределение - перезапись


c1 = Child()
print('цвет глаз ребенка:', c1.eyes)
print('возраст ребенка:', c1.age)


class Figure:
    pi = 3.1415
    e = 2.79
    name = 'Квадрат'  # Переменная (атрибут) Доступна без создания экземпляра

    def __init__(self, side1: float | int, side2: float | int):  # методы - функции внутри класса
        self.name = 'Прямоугольник'  # Переменная (экземпляра) доступна только при создании экземпляра

        self.side1 = side1
        self.side2 = side2

        # self.perimeter = (side1 + side2) * 2  # только если нагрузка небольшая (быстро и недорого для памяти)
        # self.area = side1 * side2

        self.description = 'PUBLIC'  # публичная
        self._description = 'PROTECTED'  # защищенная
        self.__description = 'PRIVATE'  # приватная

    def get_perimeter(self):  # self - ссылка на себя
        time.sleep(0.1)
        return (self.side1 + self.side2) * 2

    def get_area(self):  # self - ссылка на себя
        return self.side1 * self.side2

    def get_area_with_multiply(self, multiply: int | float) -> int | float:  # self - ссылка на себя
        return self.get_area() * multiply

    # def area
    pass


print('\n\n\n\n')
f1 = Figure(10, 15)
print('Figure1: ', f1.get_perimeter())
print('Figure1: ', f1.get_area())
print('Figure1: ', f1.get_area_with_multiply(10))
print('Figure1: ', f1.name)
print('Figure1: ', Figure.name)
print('Figure1: ', f1.description)
print('Figure1: ', f1._description)  # TODO НЕЖЕЛАТЕЛЬНО
print('Figure1: ', f1._Figure__description)  # TODO НЕЛЬЗЯ (ОПАСНО ДЛЯ ЖИЗНИ)

print('\n\n\n\n\n')


class Calc:
    def __init__(self, val1: int | float, val2: int | float, action: str = '+'):
        self.val1 = val1
        self.val2 = val2
        self.action = action

    def get_result(self, action: str = None):
        if action is not None:
            self.action = action
        match self.action:
            case '+':
                return self.val1 + self.val2
            case '-':
                return self.val1 - self.val2
            case '*':
                return self.val1 * self.val2
            case '/':
                if self.val2 != 0:
                    return self.val1 / self.val2
                else:
                    return "Error: Division by zero"
            case _:
                return "Error: Invalid action"


calc1 = Calc(5, 5, '*')
print(calc1.get_result())
print(calc1.get_result(action='-'))


class Transport:
    def __init__(self, name, mass, motor, price, speed):
        self.name = name
        self._mass = mass
        self.motor = motor
        self.price = price
        self.speed = speed  # публичная - видна во всех случаях

        self._multiplayer = 12  # защищённая - предупреждает, при попытке её извлечь вне собственного контекста
        self.__multiplayer = 10  # приватная - невидима везде, кроме собственного контекста

    def drive(self):
        return self._mass / self.motor

    def get_speed(self):
        return self.speed


Transport1 = Transport("Трактор", 2000, 400, 5000, 30)

print(Transport1)
print(type(Transport1))
print(Transport1.drive())
print(Transport1.speed)
print(Transport1._mass)
print(Transport1._multiplayer)


class Water(Transport):
    def __init__(self, speed, *args):
        super().__init__(*args)

        self.speed1 = speed

    def drive(self):
        return super().drive() / 0.85

    def get_old_speed(self):
        return super().get_speed()


Transport2 = Water(1000, "Катамаран", 500, 20, 700, 15)

print(Transport2)
print(type(Transport2))
print(Transport2.drive())
print(Transport2.speed)
print(Transport2.speed1)


class SubWater(Water):
    def __init__(self, *args, **kwargs):  # args - позиционные - кортеж, kwargs - именные - словарь
        super().__init__(*args, **kwargs)

    def drive(self):
        return super().drive() * 1.5


Transport3 = Water(333333, "Подлодка", 333, 33, 3333, 3)

dict1 = {"speed": 12}
val1 = dict1.get("speed", "")
val2 = dict1["speed"]

print(Transport3)
print(type(Transport3))
print(Transport3.drive())
print(Transport3.speed)
print(Transport3._mass)
print(Transport3.speed1)
print(Transport3.get_speed())


########################################################################################################################

########################################################################################################################
# TODO статические методы

class Utils:
    class DateTimeC:
        @staticmethod  # статический (не имеет отношения к экземпляру) метод
        def get_time():
            return datetime.datetime.now().strftime("%Y")

        @staticmethod
        def get_different_times_in_seconds(datetime1: datetime.datetime, datetime2: datetime.datetime) -> int:
            # datetime1 - datetime2
            return 0


print(Utils.DateTimeC.get_time())


########################################################################################################################

########################################################################################################################
# TODO множественное наследование

class Mother2:
    val1 = 12

    def __init__(self, val1, name="Мама") -> None:
        self.name = name
        self.val = val1
        self._val = val1  # защищённый
        self.__val2 = val1 + 5  # приватный

    def get_value(self):
        return 777

    def __str__(self):
        return self.name


class Father2:
    val2 = 13

    def __init__(self, val1) -> None:
        self.val1 = val1

    def get_value(self):
        return 888

    def __str__(self):
        return self.val1


class Child2(Father2, Mother2):

    def __init__(self, val1) -> None:
        super().__init__(val1)

    # def get_value(self):
    #     return 666


print(Mother2.val1)
a1 = Mother2(10)
print(a1.val)
# print(a1._Mother__val2)

ch1 = Child2(10)
print("\n\n\n")
print(ch1.get_value())


# TODO classmethod and staticmethod

class Person:
    population = 0  # Статическая переменная класса

    def __init__(self, name):
        self.name = name
        Person.population += 1

    @staticmethod
    def static_method():
        return "Это статический метод"

    @classmethod
    def class_method(cls):
        return f"Всего создано {cls.population} людей"


person1 = Person("Иван")
person2 = Person("Мария")

print(Person.static_method())  # Вызов статического метода напрямую от класса
print(Person.class_method())  # Вызов метода класса напрямую от класса
print('Вызов статического метода через экземпляр класса:',
      person1.static_method())  # Вызов статического метода через экземпляр класса
print('Вызов метода класса через экземпляр класса:',
      person2.class_method())  # Вызов метода класса через экземпляр класса
