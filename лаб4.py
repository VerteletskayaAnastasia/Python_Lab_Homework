
class Student_group:
    def __init__(self, quantity: int, average_age: float, avarage_height: float):
        """ Класс, описывающий объект Группа студентов

            :param quantity: Колличество студентов в группе
            :param average_age: Средний возраст студентов в группе
            :param avarage_height: Средний рост студентов в группе

         """
        if not isinstance(quantity, int):
            raise TypeError("Количество студентов в группе должен быть типа int")
        if quantity <= 0:
            raise ValueError("Количество студентов в группе должно быть положительным числом")
        if not isinstance(average_age, float):
            raise TypeError("Средний возраст студентов в группе должен быть типа float")
        if average_age <= 16:
            raise ValueError("Средний возраст студентов в группе должен быть больше 16")
        if not isinstance(avarage_height, float):
            raise TypeError("Средний рост студентов в группе должен быть типа float")
        if avarage_height <= 0:
            raise ValueError("Средний рост студентов в группе должен быть положительным числом")

        self._quantity = quantity #Допустим, что колличество студентов в группе не может меняться
        self.average_age =average_age
        self.average_height =avarage_height

        @property
        def quantity(self) -> int:
            return self._quantity

        def __str__(self):
            """ Метод str, возвращающий колличество, средний возраст и рост студентов в группе"""
            return f"Число студентов {self._quantity}. Средний возраст {self.average_age}.Средний рост {self.avarage_height}."

        def __repr__(self):
            """ Метод repr, возвращающий колличество, средний возраст и рост студентов в группе"""
            return f"{self.__class__.__name__}(_quantity={self._quantity!r}, average_age={self.average_age!r},avarage_height={self.avarage_height!r})"

        def total_height(self) -> float:
            """
            Функция, которая определяет примерный суммарный рост всех студентов группы.
            :return: Общее значение роста
            Примеры:
            >>> group = Student_group(20, 21.5, 189.3)
            >>> group.total_height()
            """
        def total_age(self) -> float:
            """
            Функция, которая определяет примерный суммарный возраст всех студентов группы.
            :return: Общее значение возраста
            Примеры:
            >>> group = Student_group(20, 21.5, 189.3)
            >>> group.total_age()
            """
class Student(Student_group):
    def __init__(self,quantity: int, average_age: float, avarage_height: float, age: int, height: float):
        """ Класс, описывающий объект Студент в группе

            :param age: Возраст студента в группе
            :param height: Рост студента в группе

         """
        super().__init__(quantity, average_age,avarage_height)
        if not isinstance(age, int):
            raise TypeError("Возраст студента в группе должен быть типа int")
        if age <= 16:
            raise ValueError("Возраст студента в группе должен быть больше 16 лет")
        if not isinstance(height, float):
            raise TypeError("Рост студента в группе должен быть типа float")
        if height <= 0:
            raise ValueError("Рост студента в группе должен быть положительным числом")

        self.age = age
        self.height = height

        def __str__(self):
            """ Метод str, возвращающий колличество, средний возраст и рост студентов в группе, возраст и рост заданного студента в группе"""
            return f"Число студентов {self._quantity}. Средний возраст {self.average_age}.Средний рост {self.avarage_height}. Возраст студента {self.age}. Рост студента {self.height}."

        def __repr__(self):
            """ Метод repr,  возвращающий колличество, средний возраст и рост студентов в группе, возраст и рост заданного студента в группе"""
            return f"{self.__class__.__name__}(_quantity={self._quantity!r}, average_age={self.average_age!r},avarage_height={self.avarage_height!r},age={self.age!r},height={self.height!r})"

if __name__ == "__main__":
    pass
