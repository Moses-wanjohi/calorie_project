from django.db import models
from django.utils import timezone

# Create your models here.

class FoodItem(models.Model):
    """
    Model representing a consumed food item and its calorie content.
    """
    name = models.CharField(max_length=200, help_text="Name of the food item")
    calories = models.PositiveIntegerField(help_text="Calorie count for the item")
    date_added = models.DateTimeField(
        default=timezone.now,
        help_text="Timestamp when the item was recorded"
    )

    class Meta:
        ordering = ['-date_added']
        verbose_name = "Food Item"
        verbose_name_plural = "Food Items"

    def __str__(self):
        return f"{self.name} ({self.calories} kcal)"