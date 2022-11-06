from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    def __init__(self, name: str, speed: int):
        self.speed_limit = 120
        self.train_value_increase = 2
        super().__init__(name, speed)

