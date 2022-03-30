from unittest import TestCase, main
from project.mammal import Mammal


class MammalTest(TestCase):
    def test_initialization_class(self):
        # Arrange, act

        mammal = Mammal("Manny", "Tiger", "RAWR")

        # assert
        self.assertEqual("Manny", mammal.name)
        self.assertEqual("Tiger", mammal.type)
        self.assertEqual("RAWR", mammal.sound)
        self.assertEqual("animals", mammal._Mammal__kingdom)

    def test_making_sound(self):
        mammal = Mammal("Manny", "Tiger", "RAWR")
        expected = "Manny makes RAWR"
        result = mammal.make_sound()
        self.assertEqual(expected, result)

    def test_get_kingdoms(self):
        mammal = Mammal("Manny", "Tiger", "RAWR")
        self.assertEqual("animals", mammal.get_kingdom())

    def test_mammal_info(self):
        mammal = Mammal("Manny", "Tiger", "RAWR")
        expected = "Manny is of type Tiger"
        result = mammal.info()
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
