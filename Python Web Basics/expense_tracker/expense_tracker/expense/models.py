from django.db import models


class Expense(models.Model):
    TITLE_MAX_LENGTH = 30

    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    expense_image = models.URLField()
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"[{self.id}] {self.title}"
