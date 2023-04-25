from project.core.validator import Validator

class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validator.raise_if_num_is_below_limit(6, value, "Users under the age of 6 are not allowed!")
        self.__age = value

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        Validator.raise_if_string_is_empty(value, "The title cannot be empty string!")
        self.__username = value

    def __str__(self):
        result = f"Username: {self.username}, Age: {self.age}\n" \
                 f"Liked movies:\n"

        if self.movies_liked:
            for movie in self.movies_liked:
                result += movie.details() + "\n"
        else:
            result += "No movies liked.\n"

        result += "Owned movies:\n"
        if self.movies_owned:
            for movie in self.movies_owned:
                result += movie.details() + "\n"
        else:
            result += "No movies owned."

        return result


