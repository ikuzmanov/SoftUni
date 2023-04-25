from unittest import TestCase, main
from project.pet_shop import PetShop



class PetShopTest(TestCase):

    def setUp(self) -> None:
        self.pet_shop = PetShop('Petshop')

    def test_petshop_init(self):
        name = 'Petshop'
        self.assertEqual(name, self.pet_shop.name)
        self.assertEqual({}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test_add_food_when_quantity_is_zero(self):
        error = 'Quantity cannot be equal to or less than 0'
        with self.assertRaises(ValueError) as ex:
            self.pet_shop.add_food('Pedigree', 0)
        self.assertEqual(error, str(ex.exception))

    def test_add_food_when_quantity_is_less_than_zero(self):
        error = 'Quantity cannot be equal to or less than 0'
        with self.assertRaises(ValueError) as ex:
            self.pet_shop.add_food('Pedigree', -5)
        self.assertEqual(error, str(ex.exception))

    def test_add_food_if_food_not_in_list(self):
        exp_result = {"Pedigree": 10}
        result = self.pet_shop.add_food("Pedigree", 10)
        exp_message = f"Successfully added {exp_result['Pedigree']:.2f} grams of {next(iter(exp_result))}."
        self.assertEqual(self.pet_shop.food, exp_result)
        self.assertTrue('Pedigree' in self.pet_shop.food)
        self.assertEqual(result, exp_message)

    def test_add_food_if_food_in_list(self):
        self.pet_shop.add_food("Pedigree", 10)
        self.assertEqual({'Pedigree': 10}, self.pet_shop.food)
        self.pet_shop.add_food('Pedigree', 20)
        self.assertEqual({'Pedigree': 30}, self.pet_shop.food)

    def test_add_pet_if_pet_not_in_list(self):
        pet_name = "Gosho"
        self.pet_shop.pets.append(pet_name)
        self.assertTrue(pet_name in self.pet_shop.pets)

    def test_add_pet_if_pet_in_list(self):
        pet_name = "Gosho"
        error = "Cannot add a pet with the same name"
        self.pet_shop.pets.append(pet_name)
        self.assertEqual([pet_name], self.pet_shop.pets)
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet(pet_name)
        self.assertEqual(error, str(ex.exception))

    def test_feed_pet_if_pet_not_list(self):
        error = "Please insert a valid pet name"
        self.pet_shop.add_food('Pedigree', 10)
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet('Pedigree', 'Gosho')
        self.assertEqual(error, str(ex.exception))

    def test_feed_pet_if_food_not_list(self):
        food_name = 'Pedigree'
        error = f"You do not have {food_name}"
        pet_name = "Gosho"
        self.pet_shop.add_pet(pet_name)
        result = self.pet_shop.feed_pet(food_name, pet_name)
        self.assertEqual(error, result)

    def test_feed_pet_if_food_is_less_than_100(self):
        food_name = 'Pedigree'
        pet_name = "Gosho"
        message = "Adding food..."
        self.pet_shop.pets.append(pet_name)
        self.pet_shop.food[food_name] = 10
        result = self.pet_shop.feed_pet(food_name, pet_name)
        self.assertEqual(message, result)
        self.assertEqual(1010, self.pet_shop.food[food_name])

    def test_feeding_pet(self):
        food_name = 'Pedigree'
        pet_name = "Gosho"
        message = f"{pet_name} was successfully fed"
        self.pet_shop.add_food(food_name, 1000)
        self.pet_shop.add_pet(pet_name)
        result = self.pet_shop.feed_pet(food_name, pet_name)
        self.assertEqual(900, self.pet_shop.food[food_name])
        self.assertEqual(message, result)

    def test_str_repr(self):
        name = 'Petshop'
        pet1 = 'Gosho'
        pet2 = 'Petio'
        self.pet_shop.pets.append(pet1)
        self.pet_shop.pets.append(pet2)
        exp_result = f'Shop {name}:\n' \
               f'Pets: Gosho, Petio'
        self.assertEqual(exp_result, str(self.pet_shop))


if __name__ == '__main__':
    main()
