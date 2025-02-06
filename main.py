from library import Book, Library, ConsoleInterface
from db import CSVStorage

def main():
    csv_storage = CSVStorage("books.csv")
    library = Library(storage= csv_storage)
    console = ConsoleInterface(source=library)

    while True:
        console.main_menu()



#     book_1 = Book(title="Вкусная магия", author="Пашнина Ольга", year=2018, genre="роман")
#     book_2 = Book(title="Академия проклятий", author="Елена Звездная", year=2007, genre="роман")
#
#     library.add_book(book_1)
#     library.add_book(book_2)
#
#     books = library.get_books()
#
#     for id_, book in books.items():
#         print(f'{id_}.{book.get_info()}')
#
#     print(Library.get_book_count())
#
#     query = "паш"
#     results = library.search_book(query)
#
#     if results:
#         print('Найденные книги:')
#
#         for id_, book in results.items():
#             print(f'{id_}.{book.get_info()}')
#     else:
#         print('Ничего не найдено.')
#
#     id_for_del = '2'
#     book_deleted = library.book_delete(id_for_del)
#     print(f'Удалена книга: {book_deleted.get_info()}')
#
#     for id_, book in books.items():
#         print(f'{id_}.{book.get_info()}')
#
#
if __name__ == '__main__':
    main()