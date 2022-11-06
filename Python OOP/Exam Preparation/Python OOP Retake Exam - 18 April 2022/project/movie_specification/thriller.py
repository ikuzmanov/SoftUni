from project.movie_specification.movie import Movie


class Thriller(Movie):
    def __init__(self, title: str, year: int, owner: object, age_restriction=16):
        self.limit = 16
        super().__init__(title, year, owner, age_restriction)

