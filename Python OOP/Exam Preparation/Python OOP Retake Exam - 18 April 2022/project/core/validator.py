class Validator:
    @staticmethod
    def raise_if_string_is_empty(value: str, error: str):
        if value == "":
            raise ValueError(error)

    @staticmethod
    def raise_if_num_is_below_limit(limit: int, value: int, error: str):
        if value < limit:
            raise ValueError(error)

    @staticmethod
    def raise_if_not_object_type(class_type: str, object, error: str):
        if object.__class__.__name__ != class_type:
            raise ValueError(error)

