from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    OXYGEN_NEEDED_FOR_BREATHING = 5

    def __init__(self, name: str):
        super().__init__(name, 70)
