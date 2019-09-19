from django.shortcuts import render

from tracker_app.models import Food, Meal


def home(request):
    return render(request, 'tracker_app/home.html')


def about(request):
    return render(request, 'tracker_app/about.html')


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
