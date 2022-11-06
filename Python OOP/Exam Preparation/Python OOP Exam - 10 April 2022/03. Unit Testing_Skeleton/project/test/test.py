from project.movie import Movie
from unittest import TestCase, main


class MovieTest(TestCase):
    def setUp(self) -> None:
        self.movie = Movie("Star", 2000, 8.0)
        self.movie2 = Movie("Wars", 2001, 5.0)

    def test_init(self):
        self.assertEqual("Star", self.movie.name)
        self.assertEqual(2000, self.movie.year)
        self.assertEqual(8.0, self.movie.rating)
        self.assertEqual([], self.movie.actors)
        self.assertEqual(0, len(self.movie.actors))

    def test_raises_if_name_is_blank(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.name = ""
        error = "Name cannot be an empty string!"
        self.assertEqual(error, str(ex.exception))

    def test_name_updates(self):
        self.movie.name = "Gosho"
        self.assertEqual("Gosho", self.movie.name)

    def test_raises_if_year_is_less_than_1887(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.year = 1886
        error = "Year is not valid!"
        self.assertEqual(error, str(ex.exception))

        self.movie.year = 1889
        self.assertEqual(1889, self.movie.year)

    def test_add_actor_if_not_in_list(self):
        actor = "Gosho"
        self.movie.add_actor(actor)
        self.assertEqual(["Gosho"], self.movie.actors)
        self.assertEqual(1, len(self.movie.actors))

    def test_add_actor_if_in_list(self):
        actor = "Gosho"
        self.movie.add_actor(actor)
        result = self.movie.add_actor(actor)
        error = f"{actor} is already added in the list of actors!"
        self.assertEqual(error, result)
        self.assertEqual(["Gosho"], self.movie.actors)
        self.assertEqual(1, len(self.movie.actors))

    def test_gt_rating_1(self):
        result = self.movie > self.movie2
        error = f'"{self.movie.name}" is better than "{self.movie2.name}"'
        self.assertEqual(error, result)

    def test_gt_rating_2(self):
        result = self.movie2 > self.movie
        error = f'"{self.movie.name}" is better than "{self.movie2.name}"'
        self.assertEqual(error, result)

    def test_repr(self):
        result = repr(self.movie)

        expected = f"Name: Star\n" \
                   f"Year of Release: 2000\n" \
                   f"Rating: 8.00\n" \
                   f"Cast: "

        self.assertEqual(expected, result)

        self.movie.add_actor("Petio")

        result2 = repr(self.movie)

        expected2 = f"Name: Star\n" \
                   f"Year of Release: 2000\n" \
                   f"Rating: 8.00\n" \
                   f"Cast: Petio"

        self.assertEqual(expected2, result2)

if __name__ == '__main__':
    main()
