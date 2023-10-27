# TODO Найдите количество книг, которое можно разместить на дискете


size_diskette_megabyte = 1.44
number_of_pages = 100
number_of_lines = 50
number_of_characters = 25
byte_for_character = 4
size_diskette_byte = size_diskette_megabyte * 1024 *1024
number_of_books = int(size_diskette_byte // (byte_for_character*number_of_characters*number_of_lines*number_of_pages))
print("Количество книг, помещающихся на дискету:", number_of_books)