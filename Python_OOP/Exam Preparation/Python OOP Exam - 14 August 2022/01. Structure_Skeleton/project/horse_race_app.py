from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        horse_types_mapping = {
            'Appaloosa': Appaloosa,
            'Thoroughbred': Thoroughbred
        }
        new_horse = self.get_horse_by_name(horse_name)
        if horse_type in horse_types_mapping:
            if new_horse is None:
                self.horses.append(horse_types_mapping[horse_type](horse_name, horse_speed))
                return f"{horse_type} horse {horse_name} is added."
            if new_horse.name == horse_name:
                raise Exception(f"Horse {horse_name} has been already added!")

    def add_jockey(self, jockey_name: str, age: int):
        new_jockey = self.get_jockey_by_name(jockey_name)
        if new_jockey is None:
            self.jockeys.append(Jockey(jockey_name, age))
            return f"Jockey {jockey_name} is added."
        raise Exception(f"Jockey {jockey_name} has been already added!")

    def create_horse_race(self, race_type: str):
        new_race = self.get_horse_race_by_type(race_type)
        if new_race is None:
            self.horse_races.append(HorseRace(race_type))
            return f"Race {race_type} is created."
        raise Exception(f"Race {race_type} has been already created!")

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        available_horses_by_type = [horse for horse in self.horses if
                                    horse.__class__.__name__ == horse_type and horse.is_taken is False]
        jockey_to_add = self.get_jockey_by_name(jockey_name)
        if jockey_to_add is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if len(available_horses_by_type) == 0:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if jockey_to_add.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        horse_to_add = available_horses_by_type[-1]

        jockey_to_add.horse = horse_to_add
        horse_to_add.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse_to_add.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        jockey_to_add = self.get_jockey_by_name(jockey_name)
        race_to_add = self.get_horse_race_by_type(race_type)

        if race_to_add is None:
            raise Exception(f"Race {race_type} could not be found!")
        if jockey_to_add is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if jockey_to_add.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if jockey_to_add in race_to_add.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        self.horse_races.append(race_to_add)
        self.jockeys.append(jockey_to_add)
        race_to_add.jockeys.append(jockey_to_add)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        current_race = self.get_horse_race_by_type(race_type)
        if current_race is None:
            raise Exception(f"Race {race_type} could not be found!")
        if len(current_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner_jockey = current_race.jockeys[0]
        for jockey in current_race.jockeys:
            if jockey.horse.speed > winner_jockey.horse.speed:
                winner_jockey = jockey

        return f"The winner of the {race_type} race, with a speed of {winner_jockey.horse.speed}km/h is {winner_jockey.name}! Winner's horse: {winner_jockey.horse.name}."

    def get_horse_by_name(self, horse_name: str):
        for horse in self.horses:
            if horse_name == horse.name:
                return horse
        return None

    def get_jockey_by_name(self, jockey_name: str):
        for jockey in self.jockeys:
            if jockey_name == jockey.name:
                return jockey
        return None

    def get_horse_race_by_type(self, race_type: str):
        for race in self.horse_races:
            if race_type == race.race_type:
                return race
        return None
