class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity > len(self.animals):
            if self.__budget >= price:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        workers_salaries = 0
        for worker in self.workers:
            workers_salaries += worker.salary
        if self.__budget >= workers_salaries:
            self.__budget -= workers_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        animal_care = 0
        for animal in self.animals:
            animal_care += animal.money_for_care
        if self.__budget >= animal_care:
            self.__budget -= animal_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals"
        lions = [animal for animal in self.animals if animal.__class__.__name__ == "Lion"]
        tigers = [animal for animal in self.animals if animal.__class__.__name__ == "Tiger"]
        cheetahs = [animal for animal in self.animals if animal.__class__.__name__ == "Cheetah"]

        result += f'\n----- {len(lions)} Lions:'
        for lion in lions:
            result += f"\n{lion}"

        result += f'\n----- {len(tigers)} Tigers:'
        for tiger in tigers:
            result += f"\n{tiger}"

        result += f'\n----- {len(cheetahs)} Cheetahs:'
        for cheetah in cheetahs:
            result += f"\n{cheetah}"

        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers"
        keepers = [worker for worker in self.workers if worker.__class__.__name__ == "Keeper"]
        caretakers = [worker for worker in self.workers if worker.__class__.__name__ == "Caretaker"]
        vets = [worker for worker in self.workers if worker.__class__.__name__ == "Vet"]

        result += f'\n----- {len(keepers)} Keepers:'
        for keeper in keepers:
            result += f"\n{keeper}"

        result += f'\n----- {len(caretakers)} Caretakers:'
        for caretaker in caretakers:
            result += f"\n{caretaker}"

        result += f'\n----- {len(vets)} Vets:'
        for vet in vets:
            result += f"\n{vet}"
        return result
