class Book:
    def __init__(self, name: str,author: str):
        """ Класс, описывающий объект Книга

                    :param name: Название книги
                    :param author: Автор книги

                 """
        self._name = name
        self._author = author

    @property
    def name(self)-> str:
        return self._name

    @property
    def author(self)-> str:
        return self._author

    def __str__(self):
        """ Метод str, возвращающий имя и автора книги"""
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        """ Метод repr, возвращающий имя и автора книги"""
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

class PaperBook(Book):
    def __init__(self,name: str, author: str, pages: int):
        """ Класс, описывающий объект Бумажная Книга

                            :param name: Название книги
                            :param author: Автор книги
                            :param pages: Число страниц книги

                         """
        super().__init__(name, author)
        self.pages = pages
    @property
    def pages(self) -> str:
        return self._pages

    @pages.setter
    def pages(self, new_pages: str) -> str:
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages

    def __repr__(self):
        """ Метод repr, возвращающий имя,автора книги, число страниц"""
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r},pages={self.pages!r})"

class AudioBook(Book):
    def __init__(self,name: str, author: str,  duration: float):
        """ Класс, описывающий объект Аудиокнига

                                    :param name: Название книги
                                    :param author: Автор книги
                                    :param duration: Продолжительность книги

                                 """
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> float:
        if not isinstance(new_duration, (int, float)):
            raise TypeError("Продолжительность должна быть типа int или float")
        if new_duration <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = new_duration

    def __repr__(self):
        """ Метод repr, возвращающий имя,автора книги, продолжительность"""
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r},duration={self.duration!r})"



