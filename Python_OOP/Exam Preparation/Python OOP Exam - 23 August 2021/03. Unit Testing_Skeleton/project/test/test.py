from project.library import Library
from unittest import TestCase, main


class LibraryTest(TestCase):
    def setUp(self) -> None:
        self.library = Library("Teka1")

    def test_init(self):
        name = "Teka1"
        books = {}
        readers = {}

        self.assertEqual(name, self.library.name)
        self.assertEqual(books, self.library.books_by_authors)
        self.assertEqual(readers, self.library.readers)

    def test_if_name_is_blank_string(self):
        name = "Teka1"
        error = "Name cannot be empty string!"
        self.assertEqual(name, self.library.name)
        with self.assertRaises(ValueError) as ex:
            self.library.name = ""
        self.assertEqual(error, str(ex.exception))

    def test_add_book(self):
        author = "Gosho"
        title = "Knijka"
        title2 = "Knijka2"

        self.library.add_book(author, title)
        self.assertEqual({"Gosho": ["Knijka"]}, self.library.books_by_authors)
        self.assertEqual(True, title in self.library.books_by_authors[author])
        self.assertEqual(1, len(self.library.books_by_authors[author]))

        self.library.add_book(author, title2)
        self.assertEqual({"Gosho": ["Knijka", "Knijka2"]}, self.library.books_by_authors)
        self.assertEqual(True, title2 in self.library.books_by_authors[author])
        self.assertEqual(2, len(self.library.books_by_authors[author]))

    def test_add_reader_if_not_in_list(self):
        reader = "Petko"
        self.library.add_reader(reader)
        self.assertEqual({reader: []}, self.library.readers)
        self.assertEqual([], self.library.readers[reader])
        self.assertEqual(1, len(self.library.readers))
        self.assertEqual(True, reader in self.library.readers)

    def test_add_reader_if_already_added(self):
        reader = "Petko"
        error = f"{reader} is already registered in the {self.library.name} library."
        self.library.add_reader(reader)
        result = self.library.add_reader(reader)
        self.assertEqual(error, result)
        self.assertEqual(1, len(self.library.readers))
        self.assertEqual(True, reader in self.library.readers)

    def test_rent_book_if_reader_not_in_list(self):
        reader = "Petko"
        book_author = "Gosho"
        book_title = "Knijka"
        error = f"{reader} is not registered in the {self.library.name} Library."
        self.library.add_book(book_author, book_title)
        result = self.library.rent_book(reader, book_author, book_title)
        self.assertEqual(error, result)
        self.assertEqual(True, book_author in self.library.books_by_authors)
        self.assertEqual(True, book_title in self.library.books_by_authors[book_author])
        self.assertEqual(True, reader not in self.library.readers)

    def test_rent_book_if_author_not_in_list(self):
        reader = "Petko"
        book_author = "Gosho"
        book_title = "Knijka"
        error = f"{self.library.name} Library does not have any {book_author}'s books."
        self.library.add_reader(reader)
        result = self.library.rent_book(reader, book_author, book_title)
        self.assertEqual(error, result)
        self.assertEqual(True, book_author not in self.library.books_by_authors)
        self.assertEqual(True, reader in self.library.readers)

    def test_rent_book_if_title_not_in_list(self):
        reader = "Petko"
        book_author = "Gosho"
        book_title = "Knijka"
        book_title_2 = "Knijka2"
        error = f"""{self.library.name} Library does not have {book_author}'s "{book_title_2}"."""
        self.library.add_reader(reader)
        self.library.add_book(book_author, book_title)
        result = self.library.rent_book(reader, book_author, book_title_2)
        self.assertEqual(error, result)
        self.assertEqual(True, book_title_2 not in self.library.books_by_authors[book_author])
        self.assertEqual(1, len(self.library.books_by_authors[book_author]))
        self.assertEqual([book_title], self.library.books_by_authors[book_author])

    def test_rent_book_success(self):
        reader = "Petko"
        book_author = "Gosho"
        book_title = "Knijka"
        self.library.add_reader(reader)
        self.library.add_book(book_author, book_title)
        self.library.rent_book(reader, book_author, book_title)
        self.assertEqual({reader: [{book_author: book_title}]}, self.library.readers)
        self.assertEqual(True, {book_author: book_title} in self.library.readers[reader])
        self.assertEqual(True, book_title not in self.library.books_by_authors[book_author])

if __name__ == '__main__':
    main()
