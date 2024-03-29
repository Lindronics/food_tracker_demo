from django import template

register = template.Library()


@register.simple_tag()
def multiply(a, b, *args, **kwargs):
    """ Simple multiplication function """
    return round(a * b, 2)


@register.simple_tag()
def food_product(food_amount, key, *args, **kwargs):
    """ Template tag for getting true calory (etc.) values of FoodAmounts.

        Takes a FoodAmount object and an attribute name (key)
        Returns the attribute value per gram multiplied by the amount
    """
    return round(food_amount.amount * getattr(food_amount.food, key), 2)


@register.simple_tag()
def food_product_mult(food_amount, multiplier, key, *args, **kwargs):
    """ Template tag for getting true calory (etc.) values of FoodAmounts 
        multiplied with a constant.

        Takes a FoodAmount object, multiplier and an attribute name (key)
        Returns the food_product times the multiplier
    """
    return round(food_product(food_amount, key) * multiplier, 2)


@register.simple_tag()
def meal_product(meal, amount, key, *args, **kwargs):
    """ Template tag function for getting true calory (etc.) values of Meals.

        Takes a Meal object, an amount and attribute name (key)
        Returns the food_product multiplied by the amount
    """
    products = [food_product(amount, key)
                for amount in meal.ingredients.all()]
    return round(sum(products) * amount, 2)


@register.simple_tag()
def total_product(food_logs, meal_logs, key, *args, **kwargs):
    """ Template tag for getting total sum of calory (etc.) values 
        of all logged foods and meals.

        Takes lists of FoodLog and MealLog objects and an attribute name (key)
        Returns the total sum over the key attribute
    """
    total = sum(meal_product(m.meal, m.amount, key) for m in meal_logs) + \
        sum(food_product(f.food_amount, key) for f in food_logs)
    return round(total, 2)
