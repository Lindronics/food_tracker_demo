import os
import django
from tqdm import tqdm
from django.core import serializers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_tracker_demo.settings')
django.setup()

from tracker_app.models import Food, FoodLog, FoodAmount, Meal, MealLog


DATA_DIR = 'sample_data'

def read_sample_data(path):
    with open(path, 'r') as f:
        for item in serializers.deserialize('json', f):
            item.save()


print('\nCreating test user...')
try:
    user = django.contrib.auth.models.User.objects.create_user('test', 'test@test.com', 'test')
    print('User created successfully')
except django.db.utils.IntegrityError:
    print('User already exists.')


print('Populating database with sample data...')
files = sorted(os.listdir(DATA_DIR))
for fname in tqdm(files):
    read_sample_data(os.path.join(DATA_DIR, fname))
print(f'Successfully deserialized and added all files in {DATA_DIR}\n')

