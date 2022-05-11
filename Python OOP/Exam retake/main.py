from project.movie_specification.action import Action
from project.movie_specification.fantasy import Fantasy
from project.movie_specification.thriller import Thriller
from project.user import User

myuser = User("Gosho", 55)
mymovie = Fantasy("Koliovite manji", 1999, myuser, 12)
movie2 = Thriller("Obiistvoto na kitaeca", 1992, myuser, 18)
movie3 = Action("Obiistvoto na kitaeca 2", 2002, myuser, 12)
print(mymovie.details())
print(movie2.details())
print(movie3.details())
print()
print(myuser)