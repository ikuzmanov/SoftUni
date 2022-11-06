from project.core.validator import Validator


class Player:
    all_players_names = []

    def __init__(self, name: str, age: int, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina
        self.__need_sustenance = True if self.stamina < 100 else False
        self.winner = False


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_string_is_empty(value, "Name not valid!")
        Validator.raise_if_duplicated_player(value, Player.all_players_names, f"Name {value} is already used!")
        Player.all_players_names.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validator.raise_if_num_is_less_than_12(value, "The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        Validator.raise_if_num_is_less_than_or_more_than_100(value, "Stamina not valid!")
        self.__need_sustenance = True
        self.__stamina = value

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.__need_sustenance}"

    def __lt__(self, other):
        if self.stamina < other.stamina:
            return True
        return False

    def __gt__(self, other):
        if self.stamina > other.stamina:
            return True
        return False

    def attack(self, other):
        stamina_to_reduce = self.stamina * 0.5
        if other.stamina - stamina_to_reduce <= 0:
            other.stamina = 0
            self.winner = True
        else:
            other.stamina -= stamina_to_reduce
