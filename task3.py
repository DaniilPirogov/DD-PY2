
class Book:     # Создаём класс "Book"
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):     # Создаём экземпляр класса с аргументами "name" и "author"
        self._name = name       # предоставляем доступ к атрибутам экземпляра класса. self
        self._author = author   # является ссылкой на текущий экземпляр класса

    @property                   # Декоратором помечаем метод "name" как свойство класса,
    def name(self) -> str:      # чтобы обращаться к методу как к атрибуту объекта.
        return self._name       # определяем метод "name", который принимает аргумент
                                # "self" и возвращает значение "self._name" типа "str".
    @property   # Аналогично примеру выше
    def author(self) -> str:    #
        return self._author     #

    def __str__(self):      # определяем метод "str" для представления экземпляра класса в виде строки
        return f"Книга {self.name}. Автор {self.author}"    # возвращаем f-строку, содержащую название книги и ее автора
    """
    Метод __repr__ возвращает строковое представление объекта, содержащее имя класса,
    выраженное с помощью self.__class__.__name__, а также имя атрибута self.name и 
    атрибут автора self.author, заключенные в круглые скобки. Каждый атрибут представлен 
    с помощью !r, что означает, что он будет представлен в виде raw string (необработанная строка).
    """
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

class PaperBook(Book):      # определяем  класс PaperBook, который наследует от класса Book
    def __init__(self, name: str, author: str, pages: int): # и имеет дополнительный интовый атрибут pages (к-во страниц)

        super().__init__(name, author)  #обращение к конструктору старшего класса
        self.pages = pages  # создаем атрибут pages для экземпляра класса и присваиваем ему значение pages

    @property   # определяем метод "pages", который принимает аргумент
    def pages(self) -> int:     # "self" и возвращает значение "self._pages" типа "int".
        return self._pages

    @pages.setter #декоратор @pages.setter устанавливает метод pages() в качестве сеттера (установщика) для свойства pages.
    def pages(self, new_pages) -> None: # Метод pages() принимает единственный аргумент new_pages, который представляет новое значение свойства pages.
        """
        Метод проверяет, является ли переданное значение new_pages целым числом с помощью
        функции isinstance(new_pages, int). Если нет, то вызывается исключение TypeError
        с сообщением "It should be 'int' here".
        """
        if not isinstance(new_pages, int):
            raise TypeError(' It should be "int" here')
        """
        Если значение new_pages меньше 1, вызывается исключение 
        ValueError с сообщением "Положительное кол-во страниц".
        """
        if new_pages < 1:
            raise ValueError('Положительное кол-во страниц')
        """
        Если все проверки прошли успешно, значение new_pages присваивается 
        приватному члену данных _pages.
        """
        self._pages = new_pages
    """ получаем строковое представление объекта, указываем как он должен выглядеть """
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

class AudioBook(Book):       # определяем  класс AudioBook, который наследует от класса Book
    def __init__(self, name: str, author: str, duration: float):

        super().__init__(name, author)  # обращение к конструктору старшего класса
        self.duration = duration  # создаем атрибут duration для экземпляра класса и присваиваем ему значение duration

    @property   # определяем метод "duration", который принимает аргумент
    def duration(self) -> float:     # "self" и возвращает значение "self._duration" типа "float".
        return self._duration
    """ декоратор @duration.setter устанавливает метод duration() в качестве сеттера (установщика) для свойства duration"""
    @duration.setter
    def duration(self, new_duration) -> None:   # Метод duration() принимает аргумент new_duration, который представляет новое значение свойства duration.
        """
        Метод проверяет, является ли переданное значение new_duration флотовым числом с помощью
        функции isinstance(new_duration, float). Если нет, то вызывается исключение TypeError
        с сообщением "It should be 'float' here".
        """
        if not isinstance(new_duration, float):
            raise TypeError(' It should be "float" here')
        """
        Если значение new_duration меньше 0, вызывается исключение 
        ValueError с сообщением "Положительное кол-во".
        """
        if new_duration <= 0:
            raise ValueError('Положительное кол-во')

        self._duration = new_duration

    """ получаем строковое представление объекта, указываем как он должен выглядеть """
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
"""вызоваем класс как функцию и передаём по 3 аргумента"""
book_1 = PaperBook("Name1", "Author1", 111) # создание экземпляра класса PaperBook
book_2 = AudioBook("Name2", "Author2", 22.2) # создание экземпляра класса AudioBook

print(book_1)
print(book_2)
print()
""" выводим строковое представление метода __repr__ """
print(book_1.__repr__)
print(book_2.__repr__)
