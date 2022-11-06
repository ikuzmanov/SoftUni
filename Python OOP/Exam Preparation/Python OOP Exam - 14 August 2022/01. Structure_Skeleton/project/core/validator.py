class Validator:
    @staticmethod
    def raise_if_less_than_limit(value, limit: int, error: str):
        if len(value) < limit:
            raise ValueError(error)

    @staticmethod
    def raise_if_string_is_empty_or_whitespace(value: str, error: str):
        if value == "" or value.isspace():
            raise ValueError(error)

    @staticmethod
    def raise_if_horse_speed_is_greater_than(value: int, speed_limit: int, error: str):
        if value > speed_limit:
            raise ValueError(error)

    @staticmethod
    def raise_if_race_type_not_valid(value):
        if value not in ("Winter", "Spring", "Autumn", "Summer"):
            raise ValueError("Race type does not exist!")
