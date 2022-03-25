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
        result = f"Table {table_number} ordered:\n"
        food_menu_names = [food.name for food in self.food_menu]
        missing_foods = []
        table = [table for table in self.tables_repository if table_number == table_number][0]
        if not table:
            return f"Could not find table {table_number}"

        for food_input in food_args:
            if food_input not in food_menu_names:
                missing_foods.append(food_input)

        for food_input in food_args:
            for food in self.food_menu:
                if food.name == food_input:
                    table.order_food(food)
                    result += repr(food) + '\n'

        result += f'{self.name} does not have in the menu:\n' + '\n'.join(missing_foods)

        return result

    def order_drink(self, table_number: int, *drink_args):
        result = f"Table {table_number} ordered:\n"
        drink_menu_name = [drink.name for drink in self.drinks_menu]
        missing_drinks = []
        table = [table for table in self.tables_repository if table_number == table_number][0]
        if not table:
            return f"Could not find table {table_number}"

        for drink_input in drink_args:
            if drink_input not in drink_menu_name:
                missing_drinks.append(drink_input)

        for drink_input in drink_args:
            for drink in self.drinks_menu:
                if drink.name == drink_input:
                    table.order_food(drink)
                    result += repr(drink) + '\n'

        result += f'{self.name} does not have in the menu:\n' + '\n'.join(missing_drinks)

        return result

    def leave_table(self, table_number: int):
        table = [table for table in self.tables_repository if table_number == table_number][0]
        table_bill = table.get_bill()
        self.total_income += table_bill
        table.clear()
        return f"Table: {table_number}\nBill: {table_bill:.2f}"

    def get_free_tables_info(self):
        result = ""
        for table in self.tables_repository:
            result += table.free_table_info() + "\n"

        return result

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
