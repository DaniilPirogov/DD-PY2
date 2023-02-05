import doctest

class Point:

    def __init__(self, color: str, radius: int, x: int, y: int):
        """
                Создание и подготовка к работе объекта "Точка"
                :param color: Цвет точки
                :param radius: Радиус точки
                :param x: Координата 'X'
                :param y: Координата 'Y'
                Примеры:
                >>> pt_1 = Point('red', 1, 1, 1)  # инициализация экземпляра класса
                >>> pt_2 = Point('black', 1, 2, 3)  # инициализация экземпляра класса
                """
        if not isinstance(color, str):
            raise TypeError("название цвета должно быть типа str")
        if not isinstance(radius, int):
            raise TypeError("Радиус должен быть типа int")
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        if not isinstance(x, int):
            raise TypeError("Координата 'x' должна быть типа int")
        if x <= 0:
            raise ValueError("Координата 'x' должна быть положительным числом")
        if not isinstance(y, int):
            raise TypeError("Координата 'y' должна быть типа int")
        if y <= 0:
            raise ValueError("Координата 'y' должна быть положительным числом")

        self.colour = color
        self.radius = radius
        self.x = x
        self.y = y

    def get_coords(self) -> str:
        """
                Функция выводит координаты точки
                :return: f"Координаты точки:  {self.x};{self.y}"
                """

    def get_area(self) -> float:
        """
                Функция выводит площадь точки
                :return: f"Площадь: {self.radius * 3.14}"
                """

class Student:

    def __init__(self, s_name: str, surname: str, age: int, course: int):
        """
                Создание и подготовка к работе объекта "Студент"
                :param s_name: имя
                :param surname: фамилия
                :param age: возраст
                :param course: номер курса
                Примеры:
                >>> st_1 = Student('Иван', 'Иванов', 18, 1)  # инициализация экземпляра класса
                >>> st_2 = Student('Денис', 'Денисов', 19, 5)  # инициализация экземпляра класса
                """
        if not isinstance(s_name, str):
            raise TypeError("Имя человека должно быть типа str")
        if not isinstance(surname, str):
            raise TypeError("Фамилия человека должна быть типа str")
        if not isinstance(age, int):
            raise TypeError("Возраст должен быть типа int")
        if age < 16:
            raise ValueError("Не бывает студентов моложе 16-ти")
        if not isinstance(age, int):
            raise TypeError("Возраст должен быть типа int")
        if 1 > course or 6 < course:
            raise ValueError("Нет такого курса")

        self.name = s_name
        self.surname = surname
        self.age = age
        self.course = course

    def get_admission_age(self) -> int:
        """
            Функция выводит возраст поступления студента
            :return: f"Возраст поступления студента {self.name[0]}.{self.surname} равен:  {self.age - self.course + 1}"
            """
    def _is_adult(self) -> bool:
        """
            Функция проверяет, является ли студент совершеннолетним
            :return: self.age >= 18
            """

class Animal:
    def __init__(self, type, name, color, iq):
        """
                Создание и подготовка к работе объекта "Животное"
                :param type: вид
                :param name: кличка
                :param color: цвет
                :param iq: уровень интеллекта
                Примеры:
                >>> an_1 = Animal('Кот', 'Барсик', 'Синий', 110)  # инициализация экземпляра класса
                >>> an_2 = Animal('Собака', 'Шарик', 'Белый', 89)  # инициализация экземпляра класса
                """
        self.type = type
        self.name = name
        self.color = color
        self.iq = iq
    def _is_clever(self) -> bool:
        """
            Умён ли ваш питомец
            :return: self.iq >= 100
            """
    def _is_cat(self) -> bool:
        """
            Ваш питомец - кот?
            :return: self.type.lower() == 'кот'
            """




if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
