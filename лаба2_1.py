# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class AppleFruit:
    def __init__(self, apple_weight:float, apple_volume:float ):
        """
            Создание и подготовка к работе объекта "Плод яблока"

            :param apple_weight: Масса яблока
            :param apple_volume: Объем яблока

            Примеры:
            >>> apple = AppleFruit(3, 100)  # инициализация экземпляра класса
            """
        if not isinstance(apple_volume, (int, float)):
            raise TypeError("Объем яблока должен быть типа int или float")
        if apple_volume <= 0:
            raise ValueError("Объем яблока должен быть положительным числом")
        self.apple_volume = apple_volume
        if not isinstance(apple_weight, (int, float)):
            raise TypeError("Масса яблока должно быть int или float ")
        if apple_weight < 0:
            raise ValueError("Масса яблока не может быть отрицательным числом")
        self.apple_weight = apple_weight

    def find_apple_density(self) -> float:
        """
        Функция которая считает плотность яблока

        :return: Значение плотности

        Примеры:
        >>> apple = AppleFruit(3, 100)
        >>> apple.find_apple_density()
        """
        ...

    def is_apple_fresh (self,days_number: int) -> bool:
        """
                   Функция которая определяет свежесть яблока
                   :param days_number: Число дней хранения яблока

                   :return: Свежее или нет

                   Примеры:
                   >>> apple = AppleFruit(3, 100)
                   >>> apple.is_apple_fresh(3)
                   """
        if not isinstance(days_number, int):
            raise TypeError("Число дней должно быть типа int")
        if days_number < 0:
            raise ValueError("Число дней должно быть положительным числом")
        ...
class ApplePie:
    def __init__(self, apple_number: int, apple_type: str):
        """
                    Создание и подготовка к работе объекта "Пирог из яблок"

                    :param apple_number: Число яблок
                    :param apple_type: Сорт яблока

                    Примеры:
                    >>> pie = ApplePie(3, 'Антоновка')  # инициализация экземпляра класса
                    """
        if not isinstance(apple_number, int):
            raise TypeError("Число яблок должно быть типа int")
        if apple_number < 0:
            raise ValueError("Число яблок должно быть положительным числом")
        self.apple_number = apple_number
        if not isinstance(apple_type, str):
            raise TypeError("Сорт яблок должен быть типа str")
    def count_pies (self) -> int:
        """
               Функция которая считает сколько пирогов можно выпечь из яблок

               :return: Число пирогов

               Примеры:
               >>> pie = ApplePie(3, 'Антоновка')
               >>> pie.count_pies()
               """
        ...

    def pie_price(self) -> float:
        """
               Функция которая считает стоимость одного пирога исходя из сорта яблок

               :return: Цена пирога

               Примеры:
               >>> pie = ApplePie(3, 'Антоновка')
               >>> pie.pie_price()
               """
        ...
class AppleJuice:
    def __init__(self, juice_ph:float, juice_volume:float ):
        """
            Создание и подготовка к работе объекта "Яблочный сок"

            :param juice_ph: Уровень pH яблочного сока
            :param juice_volume: Объем яблочного сока

            Примеры:
            >>> juice = AppleJuice(3.1, 100)  # инициализация экземпляра класса
            """
        if not isinstance(juice_ph, (int, float)):
            raise TypeError("Уровень pH яблочного сока должен быть типа int или float")
        if juice_ph < 0 or juice_ph > 14:
            raise ValueError("Уровень pH яблочного сока должен быть от 0 до 14")
        self.juice_ph = juice_ph
        if not isinstance(juice_volume, (int, float)):
            raise TypeError("Объем яблочного сока должен быть типа int или float")
        if juice_volume <= 0:
            raise ValueError("Объем яблочного сока должен быть положительным числом")
        self.juice_volume = juice_volume
    def is_ph_normal (self, normal_ph:float) -> bool:
        """
               Функция которая сравнивает значение ph с нормальным

               :param normal_ph: Нормальный уровень pH для яблочного сока

               :return: Попадает ли уровень pH в допустимый диапазон или нет

               Примеры:
               >>> juice = AppleJuice(3.1, 100)
               >>> juice.is_ph_normal(3)
               """
        ...
        if not isinstance(normal_ph, (int, float)):
            raise TypeError("Нормальный уровень pH должен быть типа int")
        if normal_ph < 0 or normal_ph > 14:
            raise ValueError("Нормальный уровень pH яблочного сока должен быть от 0 до 14")
    def count_cans (self,cans_volume:float ) -> int:
        """
                       Функция которая считает сколько банок можно наполнить соком

                       :param cans_volume: Объем одной банки

                       :return: Число банок

                       Примеры:
                       >>> juice = AppleJuice(3.1, 100)
                       >>> juice.count_cans (100)
                       """
        ...
        if not isinstance(cans_volume, (int, float)):
            raise TypeError("Объем банки должен быть типа int или float")
        if cans_volume < 0:
            raise ValueError("Объем банки должен быть положительным числом")

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
