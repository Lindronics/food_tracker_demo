from django.shortcuts import render

from tracker_app.models import Food


def home(request):
    return render(request, 'tracker_app/home.html')


def about(request):
    return render(request, 'tracker_app/about.html')


def food(request):
    context = {
        'foods': Food.objects.all(),
    }
    return render(request, 'tracker_app/food.html', context=context)


def meals(request):
    return render(request, 'tracker_app/meals.html')


def community(request):
    return render(request, 'tracker_app/community.html')
