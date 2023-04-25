from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon):
        if any([x.name == pokemon.name for x in self.pokemons]):
            return "This pokemon is already caught"
        else:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name):
        for pokemon_object in self.pokemons:
            if pokemon_name == pokemon_object.name:
                self.pokemons.remove(pokemon_object)
                return f"You have released {pokemon_name}"
        else:
            return "Pokemon is not caught"

    def trainer_data(self):
        string_to_return = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}"
        for pokemons_caught in self.pokemons:
            string_to_return += f"\n- {pokemons_caught.pokemon_details()}"

        return string_to_return


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
