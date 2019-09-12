from django.shortcuts import render


def home(request):
    return render(request, 'tracker_app/home.html')


def about(request):
    return render(request, 'tracker_app/about.html')


def food(request):
    return render(request, 'tracker_app/food.html')


def meals(request):
    return render(request, 'tracker_app/meals.html')


def community(request):
    return render(request, 'tracker_app/community.html')
