from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class Food(models.Model):
    '''  A food item
    Can have calory and macro nutrient information.
    Information is per gram.
    '''
    name = models.CharField(null=False, max_length=50)
    calories = models.FloatField(null=True)
    fat = models.FloatField(null=True)
    carbs = models.FloatField(null=True)
    protein = models.FloatField(null=True)


class FoodLog(models.Model):
    ''' A log of a food item '''
    food = models.ForeignKey(Food, null=False, on_delete=models.PROTECT)
    amount = models.FloatField(null=False)
    day = models.DateField(default=datetime.now)
    timestamp = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, related_name="food_logs", on_delete=models.CASCADE)


class Meal(models.Model):
    ''' A meal consisting of many food items 
    Can have a unit description outlining the meal size (e.g. "one plate")
    '''
    name = models.CharField(null=False, max_length=50)
    unit_description = models.CharField(null=True, max_length=50)
    ingredients = models.ManyToManyField(FoodLog, related_name='meals')


class MealLog(models.Model):
    ''' A log of a meal '''
    meal = models.ForeignKey(Meal, null=False, on_delete=models.PROTECT)
    amount = models.FloatField(null=False)
    day = models.DateField(default=datetime.now)
    timestamp = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, related_name='meal_logs', on_delete=models.CASCADE)
