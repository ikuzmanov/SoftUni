class Equipment:
    id = 0

    def __init__(self, name: str):
        self.name = name
        self.id = self.get_next_id()

    @classmethod
    def get_next_id(cls):
        Equipment.id += 1
        return Equipment.id

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
