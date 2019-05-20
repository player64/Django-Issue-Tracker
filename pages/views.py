from django.shortcuts import render

# Create your views here.


def home_page(request):
    return render(request, 'home.html', {'body_class': 'page index'})


def about_page(request):
    return render(request, 'about.html', {'body_class': 'page about'})


def stats_page(request):
    return render(request, 'stats.html', {'body_class': 'page stats'})
