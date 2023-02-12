if __name__ == "__main__":
    class Human:
        def __init__(self, name, age, gender):
            """
            Создаём объект Human
            :param name: str
            :param age: int
            :param gender: str
            """
            self.name = name
            self.age = age
            self.gender = gender

        def __str__(self):
            """
            Возвращаем строковое представление объекта Human
            :return: str
            """
            return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

        def __repr__(self):
            """
            Возвращаем строковое представление объекта Human, которое можно использовать для создания объекта.
            :return: str
            """
            return f"Human('{self.name}', {self.age}, '{self.gender}')"

        def introduce_myself(self):
            """
            Представляем человека
            :return: None
            """
            print(f"Hello, my name is {self.name} and I am {self.age} years old.")
    pass
