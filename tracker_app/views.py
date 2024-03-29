from datetime import datetime, timedelta

from django.shortcuts import render, redirect
from django.utils.dateparse import parse_date
from django.contrib.auth.decorators import login_required

from tracker_app.models import Food, Meal, Day, FoodLog, MealLog, User


def home(request):
    """ Home view """
    return render(request, 'tracker_app/home.html')


def about(request):
    """ About view """
    return render(request, 'tracker_app/about.html')


@login_required
def profile_today(request, username):
    """ Default profile view

        This view is called when a user navigates to Profile.
        It redirects to the profile view with the current date.
    """
    today = datetime.now().strftime('%Y-%m-%d')
    return redirect(profile, username, today)


@login_required
def profile(request, username, date):
    """ Profile view

        This view displays the user profile, as well as food and meal logs.
    """
    parsed_date = parse_date(date)
    user = User.objects.get(username=username)

    # Days are created lazily (upon user access)
    day = Day.objects.get_or_create(user=user, date=parsed_date)[0]

    food_logs = FoodLog.objects.all().filter(day=day)
    meal_logs = MealLog.objects.all().filter(day=day)

    context = {
        'username': username,
        'today': parsed_date,
        'yesterday': parsed_date - timedelta(days=1),
        'tomorrow': parsed_date + timedelta(days=1),
        'food_logs': food_logs,
        'meal_logs': meal_logs,
    }
    return render(request, 'tracker_app/profile.html', context=context)


def food(request):
    """ Food view

        Displays the database of food items.
    """
    foods = Food.objects.all()
    context = {
        'foods': foods,
        'foods_total_count': len(foods),
    }
    return render(request, 'tracker_app/food.html', context=context)


def new_food(request):
    """ New food view

        Allows creation of new food items
    """

    # If form submitted, create new food
    if request.method == 'POST':
        params = dict(request.POST.items())
        del(params['csrfmiddlewaretoken'])

        # Get values per gram
        for param in ['calories', 'fat', 'carbs', 'protein']:
            params[param] = float(params[param]) / 100.0
            
        Food.objects.create(**params)
        return redirect(food)

    return render(request, 'tracker_app/new_food.html')


def meals(request):
    """ Meals view

        Displays the database of meal items.
    """
    meals = Meal.objects.all()
    context = {
        'meals': meals,
        'meals_total_count': len(meals),
    }
    return render(request, 'tracker_app/meals.html', context=context)


def meal(request, meal_id):
    """ Meal view

        Displays details for a meal.
    """
    context = {
        'meal': Meal.objects.get(pk=meal_id),
        'portions': int(request.GET.get('portions', 1)),
    }
    return render(request, 'tracker_app/meal.html', context=context)


def community(request):
    """ Community view """
    return render(request, 'tracker_app/community.html')
