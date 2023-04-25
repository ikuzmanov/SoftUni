from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    def __init__(self, name: str, speed: int):
        self.speed_limit = 140
        self.train_value_increase = 3
        super().__init__(name, speed)
