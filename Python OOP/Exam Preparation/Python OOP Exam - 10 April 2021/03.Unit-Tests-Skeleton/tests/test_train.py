from unittest import TestCase, main

from project.train.train import Train


class TrainTest(TestCase):
    def setUp(self) -> None:
        self.train = Train("Vlakcho", 0)

    def test_init(self):
        name = "Vlakcho"
        capacity = 0
        passengers = []

        self.assertEqual(name, self.train.name)
        self.assertEqual(capacity, self.train.capacity)
        self.assertEqual(passengers, self.train.passengers)

    def test_add_passengers_when_train_is_full(self):
        error = "Train is full"
        with self.assertRaises(ValueError) as ex:
            self.train.add("Gosho")
        self.assertEqual(error, str(ex.exception))

    def test_add_passengers_if_passenger_exists(self):
        self.train.passengers = ["Gosho"]
        error = "Passenger Gosho Exists"
        with self.assertRaises(ValueError) as ex:
            self.train.add("Gosho")
        self.assertEqual(error, str(ex.exception))

    def test_add_passengers_sucessfully(self):
        self.train.capacity = 5
        result = self.train.add("Gosho")
        expected = "Added passenger Gosho"
        self.assertEqual(expected, result)

    def test_remove_passenger_if_not_found(self):
        with self.assertRaises(ValueError) as ex:
            self.train.remove("Gosho")
        error = "Passenger Not Found"
        self.assertEqual(error, str(ex.exception))

    def test_remove_passenger_sucessfully(self):
        self.train.capacity = 5
        self.train.add("Gosho")
        result = self.train.remove("Gosho")
        expected = "Removed Gosho"
        self.assertEqual(expected, result)

if __name__ == '__main__':
    main()
