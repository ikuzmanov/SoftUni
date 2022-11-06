from project.plantation import Plantation
from unittest import TestCase, main


class PlantationTest(TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(5)

    def test_init(self):
        size = 5
        plants = {}
        workers = []

        self.assertEqual(size, self.plantation.size)
        self.assertEqual(plants, self.plantation.plants)
        self.assertEqual(workers, self.plantation.workers)

    def test_raise_if_size_is_less_than_zero(self):
        size = -1
        error = "Size must be positive number!"
        with self.assertRaises(ValueError) as ex:
            self.plantation.size = size
        self.assertEqual(error, str(ex.exception))

    def test_raise_if_worker_is_already_hired(self):
        self.plantation.workers = ["Gosho", "Pesho", "Genata"]
        error = "Worker already hired!"
        with self.assertRaises(ValueError) as ex:
            self.plantation.hire_worker("Gosho")
        self.assertEqual(error, str(ex.exception))

    def test_hire_worker_successfully(self):
        worker = "Gosho"
        result = self.plantation.hire_worker(worker)
        message = f"{worker} successfully hired."
        self.assertEqual(result, message)
        self.assertEqual(["Gosho"], self.plantation.workers)
        self.assertEqual(1, len(self.plantation.workers))

    def test_plantation_length(self):
        self.plantation.plants = {"Roses": ["Red", "White"], "Tulips": ["Pink", "Green"]}
        result = len(self.plantation)
        self.assertEqual(4, result)

    def test_planting_if_worker_not_found(self):
        self.plantation.plants = {"Roses": ["Red", "White"], "Tulips": ["Pink", "Green"]}
        worker = "Gosho"
        error = f"Worker with name {worker} is not hired!"
        with self.assertRaises(ValueError) as ex:
            self.plantation.planting(worker, "Roses")
        self.assertEqual(error,str(ex.exception))

    def test_planting_if_plantation_is_full(self):
        self.plantation.plants = {"Roses": ["Red", "White"], "Tulips": ["Pink", "Green"]}
        self.plantation.workers = ["Gosho"]
        self.plantation.size = 4
        error = "The plantation is full!"
        with self.assertRaises(ValueError) as ex:
            self.plantation.planting("Gosho", "Tulip")
        self.assertEqual(error, str(ex.exception))

    def test_planting_success_more_than_one_plants(self):
        self.plantation.plants = {"Gosho": ["Red", "White"], "Pesho": ["Pink", "Green"]}
        self.plantation.workers = ["Gosho", "Pesho"]
        worker = "Gosho"
        plant = "Lavender"
        result = self.plantation.planting(worker, plant)
        message = f"{worker} planted {plant}."
        self.assertEqual(message, result)
        result2 = self.plantation.plants[worker]
        self.assertEqual(["Red", "White", "Lavender"], result2)
        self.assertEqual(3, len(self.plantation.plants[worker]))


    def test_first_planting_success(self):
        self.plantation.workers = ["Gosho", "Pesho"]
        result = self.plantation.planting("Gosho", "Lavender")
        error = f"Gosho planted it's first Lavender."
        self.assertEqual(error, result)
        self.assertEqual(1, len(self.plantation.plants["Gosho"]))
        self.assertEqual(["Lavender"], self.plantation.plants["Gosho"])


    def test_str(self):
        self.plantation.plants = {"Gosho": ["Red", "White"], "Pesho": ["Pink", "Green"]}
        self.plantation.workers = ["Gosho", "Pesho"]
        result = str(self.plantation)
        expected = "Plantation size: 5\nGosho, Pesho\nGosho planted: Red, White\nPesho planted: Pink, Green"
        self.assertEqual(expected, result)

    def test_repr(self):
        self.plantation.plants = {"Gosho": ["Red", "White"], "Pesho": ["Pink", "Green"]}
        self.plantation.workers = ["Gosho", "Pesho"]
        result = repr(self.plantation)
        expected = "Size: 5\nWorkers: Gosho, Pesho"
        self.assertEqual(expected, result)

if __name__ == '__main__':
    main()
