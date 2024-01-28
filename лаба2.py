BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

class Book:
    def __init__(self, id_, name, pages):
        """ Класс, описывающий объект Книга

            :param id_: ID книги
            :param name: Название книги
            :param pages: Количество страниц книги

         """
        if not isinstance(id_, int):
            raise TypeError("ID должно быть типа int")
        if id_ <= 0:
            raise ValueError("ID должно быть положительным числом")
        if not isinstance(name, str):
            raise TypeError("Название книги должно быть типа str")
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.id_ = id_
        self.name = name
        self.pages = pages

# TODO написать класс Library
class Library:
    def __init__(self, books=[]):
        """ Класс, описывающий объект Библиотека

                    :param books: Список книг в библиотеке

                 """
        self.books = books
    def get_next_book_id(self) -> int:
        """ Метод, возвращающий идентификатор для добавления новой книги в библиотеку """
        return len(self.books) + 1

   def get_index_by_book_id(self, book_id)-> int:
       """ Метод, возвращающий индекс книги в списке """
       for index, value in enumerate(self.books):
           if index == book_id:
               return index - 1
       raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
   empty_library = Library()  # инициализируем пустую библиотеку
   print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

   list_books = [
       Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
   ]
   library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
   print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

   print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
