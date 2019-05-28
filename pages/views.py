from django.shortcuts import render
from django.http import JsonResponse
from bugs.models import Bugs
from features.models import Features
# Create your views here.


def home_page(request):
    return render(request, 'home.html', {'body_class': 'page index'})


def about_page(request):
    return render(request, 'about.html', {'body_class': 'page about'})


def stats_page(request):
    return render(request, 'stats.html', {'body_class': 'page stats'})


def api_stats(request):
    count_statuses = {
        'bugs': {},
        'features': {}
    }

    statuses = ['todo', 'doing', 'done']
    for status in statuses:
        count_statuses['bugs'].update({
            status: Bugs.objects.filter(status=status).count()
        })
        count_statuses['features'].update({
            status: Features.objects.filter(status=status).count()
        })

    limit = 10
    voted_bugs = Bugs.objects.filter(total_votes__gte=1).order_by('-total_votes')[:limit]
    voted_features = Features.objects.filter(total_votes__gte=1).order_by('-total_votes')[:limit]

    data = {
        'statuses': count_statuses,
        'votes': {
            'bugs': create_voted_items(voted_bugs),
            'features': create_voted_items(voted_features)
        }
    }
    return JsonResponse(data)


def create_voted_items(data):
    labels = []
    votes = []

    for item in data:
        labels.append(item.name)
        votes.append(item.total_votes)

    return {
        'labels': labels,
        'votes': votes
    }
