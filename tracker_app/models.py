from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class Day(models.Model):
    """ A day containing logged meals and foods """
    date = models.DateField(default=datetime.now)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)


class Food(models.Model):
    """ A food item
        Can have calory and macro nutrient information.
        Information is per gram.
    """
    name = models.CharField(null=False, max_length=50)
    calories = models.FloatField(null=True)
    fat = models.FloatField(null=True)
    carbs = models.FloatField(null=True)
    protein = models.FloatField(null=True)


class FoodAmount(models.Model):
    """ A food item paired with an amount to be used for meals and logs """
    food = models.ForeignKey(Food, null=False, on_delete=models.PROTECT)
    amount = models.FloatField(null=False)


class FoodLog(models.Model):
    """ A log of a food item """
    food_amount = models.ForeignKey(FoodAmount, null=False, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, null=False, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.now)


class Meal(models.Model):
    """ A meal consisting of many food items 
        Can have a unit description outlining the meal size (e.g. "one plate")
    """
    name = models.CharField(null=False, max_length=50)
    description = models.CharField(default="No description", max_length=300)
    unit_description = models.CharField(null=True, max_length=50)
    ingredients = models.ManyToManyField(FoodAmount, related_name='meals')


class MealLog(models.Model):
    """ A log of a meal """
    meal = models.ForeignKey(Meal, null=False, on_delete=models.PROTECT, related_name='meal_logs')
    amount = models.FloatField(null=False)
    day = models.ForeignKey(Day, null=False, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.now)
