from datetime import datetime, timedelta

from django.shortcuts import render
from django.utils.dateparse import parse_date

from tracker_app.models import Food, Meal, Day, FoodLog, MealLog


def home(request):
    return render(request, 'tracker_app/home.html')


def about(request):
    return render(request, 'tracker_app/about.html')


def profile_today(request):
    today = datetime.now().strftime('%Y-%m-%d')
    return profile(request, today)


def profile(request, date):
    parsed_date = parse_date(date)
    
    # Days are created lazily (upon user access)
    day = Day.objects.get_or_create(user=request.user, date=parsed_date)[0]

    food_logs = FoodLog.objects.all().filter(day=day)
    meal_logs = MealLog.objects.all().filter(day=day)

    context = {
        'today': parsed_date,
        'yesterday': parsed_date - timedelta(days=1),
        'tomorrow': parsed_date + timedelta(days=1),
        'food_logs': food_logs,
        'meal_logs': meal_logs,
    }
    return render(request, 'tracker_app/profile.html', context=context)


def food(request):
    foods = Food.objects.all()
    context = {
        'foods': foods,
        'foods_total_count': len(foods),
    }
    return render(request, 'tracker_app/food.html', context=context)


def meals(request):
    meals = Meal.objects.all()
    context = {
        'meals': meals,
        'meals_total_count': len(meals),
    }
    return render(request, 'tracker_app/meals.html', context=context)


def community(request):
    return render(request, 'tracker_app/community.html')
