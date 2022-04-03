from project.baked_food.cake import Cake
from project.baked_food.bread import Bread
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    possible_food_types = ("Bread", "Cake")
    possible_drink_types = ("Tea", "Water")
    possible_table_types = ('InsideTable', 'OutsideTable')

    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    def add_food(self, food_type: str, name: str, price: float):
        if name in [food.name for food in self.food_menu]:
            raise Exception(f"{food_type} {name} is already in the menu!")
        if food_type in Bakery.possible_food_types:
            self.food_menu.append(eval(food_type)(name, price))
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if name in [drink.name for drink in self.drinks_menu]:
            raise Exception(f"{drink_type} {name} is already in the menu!")
        if drink_type in Bakery.possible_drink_types:
            self.drinks_menu.append(eval(drink_type)(name, portion, brand))
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_number in [table.table_number for table in self.tables_repository]:
            raise Exception(f"Table {table_number} is already in the bakery!")

        if table_type in Bakery.possible_table_types:
            self.tables_repository.append(eval(table_type)(table_number, capacity))
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        available_tables = [table for table in self.tables_repository if
                            number_of_people <= table.capacity and not table.is_reserved]
        if available_tables:
            first_table = available_tables[0]
            first_table.reserve(number_of_people)
            return f"Table {first_table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_args):
        table = self.find_table_by_number(table_number)
        if table is None:
            return f'Could not find table {table_number}'

        ordered_foods = f'Table {table_number} ordered:\n'
        skipped_order_foods = f'{self.name} does not have in the menu:\n'

        for food_name in food_args:
            food = self.find_food_by_name(food_name)
            if food is None:
                skipped_order_foods += food_name + '\n'
            else:
                table.order_food(food)
                ordered_foods += str(food) + '\n'

        return ordered_foods.strip() + '\n' + skipped_order_foods.strip()

    def order_drink(self, table_number: int, *drink_args):
        table = self.find_table_by_number(table_number)
        if table is None:
            return f'Could not find table {table_number}'

        ordered_drinks= f'Table {table_number} ordered:\n'
        skipped_order_drinks = f'{self.name} does not have in the menu:\n'

        for drink_name in drink_args:
            drink = self.find_drink_by_name(drink_name)
            if drink is None:
                skipped_order_drinks += drink_name + '\n'
            else:
                table.order_drink(drink)
                ordered_drinks += str(drink) + '\n'

        return ordered_drinks.strip() + '\n' + skipped_order_drinks.strip()

    def leave_table(self, table_number: int):
        table = self.find_table_by_number(table_number)
        table_bill = table.get_bill()
        self.total_income += table_bill
        table.clear()
        return f"Table: {table_number}\nBill: {table_bill:.2f}"

    def get_free_tables_info(self):
        result = ""
        for table in self.tables_repository:
            if not table.is_reserved:
                result += table.free_table_info() + "\n"
        return result.strip()

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

    def find_table_by_number(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table
        return None

    def find_food_by_name(self, food_name):
        for food in self.food_menu:
            if food.name == food_name:
                return food
        return None

    def find_drink_by_name(self, drink_name):
        for drink in self.drinks_menu:
            if drink.name == drink_name:
                return drink
        return None
