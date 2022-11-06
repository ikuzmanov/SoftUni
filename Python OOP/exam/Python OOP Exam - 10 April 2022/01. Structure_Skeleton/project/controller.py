class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        successfully_added_players = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                successfully_added_players.append(player.name)

        return f"Successfully added: {', '.join(successfully_added_players)}"

    def add_supply(self, *supplies):
        for supply in supplies:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.get_player_by_name(player_name)
        if sustenance_type in ("Food", "Drink") and player:
            if not player._Player__need_sustenance:
                return f"{player_name} have enough stamina."

            supply = self.get_supply_by_type(sustenance_type)

            if player.stamina + supply.energy > 100:
                player.stamina = 100
            else:
                player.stamina += supply.energy

            return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.get_player_by_name(first_player_name)
        second_player = self.get_player_by_name(second_player_name)
        if first_player and second_player:
            if first_player.stamina == 0:
                return f"Player {first_player.name} does not have enough stamina."
            elif second_player.stamina == 0:
                return f"Player {second_player.name} does not have enough stamina."

            if first_player < second_player:
                attacker = first_player
                defender = second_player
            else:
                attacker = second_player
                defender = first_player

            while True:
                attacker.attack(defender)
                defender.attack(attacker)
                if attacker.winner or attacker > defender:
                    return f"Winner: {attacker.name}"
                elif defender.winner or defender > defender:
                    return f"Winner: {defender.name}"
    def next_day(self):
        for player in self.players:
            stamina_to_reduce = player.age * 2
            if player.stamina - stamina_to_reduce < 0:
                player.stamina = 0
            else:
                player.stamina -= stamina_to_reduce
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = ""
        for player in self.players:
            result += str(player) + "\n"

        for supply in self.supplies:
            result += supply.details() + "\n"

        return result.strip()

    def get_player_by_name(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    @staticmethod
    def attack(attacker, defender):
        pass

    def get_supply_by_type(self, sustenance_type):
        if sustenance_type == "Food":
            food_supplies = [food for food in self.supplies if food.__class__.__name__ == "Food"]
            if not food_supplies:
                raise Exception("There are no food supplies left!")
            food_to_remove = food_supplies.pop()
            self.supplies.remove(food_to_remove)
            return food_to_remove

        if sustenance_type == "Drink":
            drink_supplies = [drink for drink in self.supplies if drink.__class__.__name__ == "Drink"]
            if not drink_supplies:
                raise Exception("There are no drink supplies left!")

            drink_to_remove = drink_supplies.pop()
            self.supplies.remove(drink_to_remove)
            return drink_to_remove
