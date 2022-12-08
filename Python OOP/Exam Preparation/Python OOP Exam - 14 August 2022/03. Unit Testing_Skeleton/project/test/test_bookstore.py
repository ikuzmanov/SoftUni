from unittest import TestCase, main
from project.bookstore import Bookstore


class BookstoreTest(TestCase):
    def setUp(self) -> None:
        self.bookstore = Bookstore(10)

    def test_init(self):
        self.assertEqual(10, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_if_book_limit_is_below_or_equal_to_zero(self):
        value = -1
        error = f"Books limit of {value} is not valid"
        with self.assertRaises(ValueError) as ex:
            self.bookstore.books_limit = value
        self.assertEqual(error, str(ex.exception))

        value_2 = 0
        error_2 = f"Books limit of {value_2} is not valid"
        with self.assertRaises(ValueError) as ex:
            self.bookstore.books_limit = value_2
        self.assertEqual(error_2, str(ex.exception))

    def test_len_bookstore(self):
        self.assertEqual(0, len(self.bookstore))
        self.bookstore.receive_book("Star Wars", 1)
        self.assertEqual(1, len(self.bookstore))

    def test_receive_book_if_not_enough_space(self):
        error = "Books limit is reached. Cannot receive more books!"
        self.bookstore.books_limit = 1
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("Star Wars", 2)
        self.assertEqual(error, str(ex.exception))

    def test_receive_book_success(self):
        title = "Star Wars"
        count = 1
        result = self.bookstore.receive_book(title, count)
        self.assertEqual(count, len(self.bookstore))
        self.assertEqual(title, next(iter(self.bookstore.availability_in_store_by_book_titles)))
        self.assertEqual(count, self.bookstore.availability_in_store_by_book_titles[title])
        self.assertEqual({title: count}, self.bookstore.availability_in_store_by_book_titles)

        expected = f"{count} copies of {title} are available in the bookstore."
        self.assertEqual(expected, result)

    def test_sell_book_book_not_available_in_bookstore(self):
        book_title = "Star Wars"
        error = f"Book {book_title} doesn't exist!"
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book(book_title, 1)
        self.assertEqual(error, str(ex.exception))
        self.assertEqual(0, len(self.bookstore))
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)

    def test_sell_book_not_enough_copies(self):
        book_title = "Star Wars"
        copies = 2
        error = f"{book_title} has not enough copies to sell. Left: {copies}"
        self.bookstore.receive_book(book_title, copies)
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book(book_title, 5)
        self.assertEqual(error, str(ex.exception))
        self.assertEqual({"Star Wars": 2}, self.bookstore.availability_in_store_by_book_titles)

    def test_sell_book_success(self):
        book_title = "Star Wars"
        copies_received = 2
        copies_sold = 1
        self.bookstore.receive_book(book_title, copies_received)
        message = f"Sold {copies_sold} copies of {book_title}"
        result = self.bookstore.sell_book(book_title, copies_sold)
        self.assertEqual(message, result)
        self.assertEqual(1, self.bookstore.total_sold_books)
        self.assertEqual({"Star Wars": 1}, self.bookstore.availability_in_store_by_book_titles)

    def test_str_repr(self):
        self.bookstore.receive_book("Star Wars", 2)
        self.bookstore.receive_book("One night", 1)
        result = str(self.bookstore)
        expected = "Total sold books: 0\nCurrent availability: 3\n - Star Wars: 2 copies\n - One night: 1 copies"
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()


def test_funct(pass):
    while True:
        print("Hi how are you?")
