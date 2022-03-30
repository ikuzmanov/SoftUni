from unittest import TestCase, main

from project.vehicle import Vehicle


class VehicleTest(TestCase):

    def test_initialization(self):
        car = Vehicle(100, 150)
        self.assertEqual(100, car.fuel)
        self.assertEqual(150, car.horse_power)
        self.assertEqual(100, car.capacity)
        self.assertEqual(1.25, car.fuel_consumption)

    def test_car_drive(self):
        car = Vehicle(0, 150)
        with self.assertRaises(Exception) as ex:
            car.drive(1000)
        self.assertEqual("Not enough fuel", str(ex.exception))
        car = Vehicle(100, 150)

        car = Vehicle(150, 150)
        car.drive(100)
        self.assertEqual(25, car.fuel)

    def test_refuel(self):
        car = Vehicle(50, 150)
        car.drive(10)
        car.refuel(12.5)
        self.assertEqual(50, car.fuel)

        car = Vehicle(50, 150)
        with self.assertRaises(Exception) as ex:
            car.refuel(12.5)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str_repr(self):
        car = Vehicle(50, 150)
        expected = f"The vehicle has 150 " \
                   f"horse power with 50 fuel left and 1.25 fuel consumption"
        result = str(car)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
