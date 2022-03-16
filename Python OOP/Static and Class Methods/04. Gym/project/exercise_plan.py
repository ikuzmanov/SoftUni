class ExercisePlan:
    id = 0

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = self.get_next_id()

    @staticmethod
    def get_next_id():
        ExercisePlan.id += 1
        return ExercisePlan.id

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        hours = hours*60
        return cls(trainer_id, equipment_id, hours)

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"


Plan1 = ExercisePlan(123, 221, 30)
Plan2 = ExercisePlan.from_hours(123, 222, 1)
a=5