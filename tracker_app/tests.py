from django.test import TestCase

from django.test import TestCase
from django.contrib.auth.models import User

from tracker_app.models import Food

class FoodTest(TestCase):
    def setUp(self):
        self.params = {
            'name': 'Ben&Jerry\'s',
            'calories': 2.45,
            'fat': 0.13,
            'carbs': 0.29,
            'protein': 0.04,
        }
        Food.objects.create(**self.params)

    def test_get_food(self):
        test_food = Food.objects.get(name=self.params['name'])
        self.assertEqual(self.params['calories'], test_food.calories)
