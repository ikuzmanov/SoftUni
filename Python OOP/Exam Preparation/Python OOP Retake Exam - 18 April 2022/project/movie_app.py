from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        for user in self.users_collection:
            if user.username == username:
                raise Exception("User already exists!")
        self.users_collection.append(User(username, age))
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie):
        current_user = self.get_user_by_username(username)
        if current_user is None:
            raise Exception("This user does not exist!")
        elif username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        elif movie in current_user.movies_owned:
            raise Exception("Movie already added to the collection!")
        else:
            current_user.movies_owned.append(movie)
            self.movies_collection.append(movie)
            return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie, **kwargs):
        current_user = self.get_user_by_username(username)
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if current_user is None or movie not in current_user.movies_owned:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        for arg in kwargs:
            if arg == "title":
                movie.title = kwargs[arg]
            elif arg == "year":
                movie.year = kwargs[arg]
            elif arg == "age_restriction":
                movie.age_restriction = kwargs[arg]

        return f"{username} successfully edited {movie.title} movie."

    def like_movie(self, username: str, movie):
        current_user = self.get_user_by_username(username)
        if movie in current_user.movies_owned:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        if movie in current_user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        current_user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie):
        current_user = self.get_user_by_username(username)
        if movie in current_user.movies_liked:
            movie.likes -= 1
            current_user.movies_liked.remove(movie)
            return f"{username} disliked {movie.title} movie."
        else:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

    def display_movies(self):
        sorted_movies = sorted(self.movies_collection, key=lambda value: (value.year, value.title), reverse=True)
        result = ""
        if sorted_movies:
            for movie in sorted_movies:
                result += movie.details() + "\n"
        else:
            result = "No movies found."
        return result.strip()

    def delete_movie(self, username: str, movie):
        current_user = self.get_user_by_username(username)
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie not in current_user.movies_owned:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        current_user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def __str__(self):
        result = "All users: "
        if self.users_collection:
            result += ', '.join([user.username for user in self.users_collection])
        else:
            result += "No users."
        result += "\nAll movies: "
        if self.movies_collection:
            result += ', '.join([movie.title for movie in self.movies_collection])
        else:
            result += "No movies."

        return result.strip()

    def get_user_by_username(self, username):
        for user in self.users_collection:
            if user.username == username:
                return user
