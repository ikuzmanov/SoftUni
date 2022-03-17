from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if not self.check_if_object_in_entity(customer.id, self.customers):
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if not self.check_if_object_in_entity(trainer.id, self.trainers):
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if not self.check_if_object_in_entity(equipment.id, self.equipment):
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if not self.check_if_object_in_entity(plan.id, self.plans):
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if not self.check_if_object_in_entity(subscription.id, self.subscriptions):
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscription = self.get_object(subscription_id, self.subscriptions)
        customer = self.get_object(subscription.customer_id, self.customers)
        trainer = self.get_object(subscription.trainer_id, self.trainers)
        exercise_plan = self.get_object(subscription.exercise_id, self.plans)
        equipment = self.get_object(exercise_plan.equipment_id, self.equipment)
        return repr(subscription) + "\n" + repr(customer) + "\n" + repr(trainer) + "\n" + repr(equipment) + "\n" + repr(exercise_plan)

    def check_if_object_in_entity(self, object_id, entity):
        for ent in entity:
            if ent.id == object_id:
                return True
            return False

    def get_object(self, obj_id, entity):
        for ent in entity:
            if ent.id == obj_id:
                return ent