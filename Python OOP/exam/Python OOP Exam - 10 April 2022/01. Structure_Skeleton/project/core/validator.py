class Validator:
    @staticmethod
    def raise_if_string_is_empty(value: str, error: str):
        if value == "":
            raise ValueError(error)

    @staticmethod
    def raise_if_num_is_less_than_zero(value: int, error: str):
        if value < 0:
            raise ValueError(error)

    @staticmethod
    def raise_if_num_is_less_than_12(value, error):
        if value < 12:
            raise ValueError(error)

    @staticmethod
    def raise_if_num_is_less_than_or_more_than_100(value, error):
        if value < 0 or value > 100:
            raise ValueError(error)

    @staticmethod
    def raise_if_duplicated_player(value, players_list, error):
        if value in players_list:
            raise Exception(error)
