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


if __name__ == '__main__':
    main()
