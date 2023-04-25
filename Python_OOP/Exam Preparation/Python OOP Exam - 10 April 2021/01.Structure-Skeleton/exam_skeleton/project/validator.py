class Validator:
    @staticmethod
    def raise_if_string_is_empty(value, attr):
        if value == "":
            raise ValueError(f"{attr} cannot be an empty string.")

    @staticmethod
    def raise_if_price_is_equal_or_below_zero(value, attr):
        if value <= 0:
            raise ValueError(f"{attr} cannot be equal to or below zero.")