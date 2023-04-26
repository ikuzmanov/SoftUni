from django.core.validators import MinValueValidator
from django.db import models
from gamesplayapp.web.validators import RatingBetweenValues


# Create your models here.
class Profile(models.Model):
    MINIMUM_AGE = 12
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30
    PASSWORD_MAX_LENGTH = 30

    email = models.EmailField()
    age = models.IntegerField(validators=(MinValueValidator(MINIMUM_AGE),))
    password = models.CharField(max_length=PASSWORD_MAX_LENGTH)
    first_name = models.CharField(max_length=FIRST_NAME_MAX_LENGTH, blank=True)
    last_name = models.CharField(max_length=LAST_NAME_MAX_LENGTH, blank=True)
    profile_picture = models.URLField(blank=True)

    def __str__(self):
        return f"{self.id}: {self.first_name} {self.last_name}"


class Game(models.Model):
    TITLE_MAX_LENGTH = 30
    CATEGORY_MAX_LENGTH = 15
    MIN_LEVEL = 1
    MIN_RATING = 0.1
    MAX_RATING = 5.0

    ACTION = "Action"
    ADVENTURE = "Adventure"
    PUZZLE = "Puzzle"
    STRATEGY = "Strategy"
    SPORTS = "Sports"
    BOARD_CARD_GAME = "Board/Card Game"
    OTHER = "Other"

    GAME_CATEGORY = (
        (ACTION, "Action"),
        (ADVENTURE, "Adventure"),
        (PUZZLE, "Puzzle"),
        (STRATEGY, "Strategy"),
        (SPORTS, "Sports"),
        (BOARD_CARD_GAME, "Board/Card Game"),
        (OTHER, "Other"),
    )

    title = models.CharField(max_length=TITLE_MAX_LENGTH, unique=True)
    category = models.CharField(max_length=CATEGORY_MAX_LENGTH, choices=GAME_CATEGORY)
    rating = models.FloatField(validators=(RatingBetweenValues(MIN_RATING, MAX_RATING),))
    max_level = models.IntegerField(validators=(MinValueValidator(MIN_LEVEL),), blank=True)
    image_url = models.URLField()
    summary = models.TextField(blank=True)

    def __str__(self):
        return f"{self.id}: {self.title}"
