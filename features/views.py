from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Features, FeatureComment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import FeatureForm, FeatureCommentForm


@login_required()
def archive(request):
    features = Features.objects.all().order_by('-total_votes', '-published')
    return render(request, 'archive.html', {'items': features, 'title': 'Features',
                                            'no_results_txt': 'Any feature has been found',
                                            'add_url': reverse('feature_new'),
                                            'body_class': 'features',
                                            'archive_name': 'features'})


@login_required()
def single(request, pk):
    feature = get_object_or_404(Features, pk=pk)
    if request.method == "POST":

        form = FeatureCommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.feature = feature
            comment.author = request.user
            comment.save()
            messages.success(request, "Comment has been added")
            return redirect(reverse('feature_single', kwargs={'pk': pk}))

    comment_form = FeatureCommentForm()
    comments = FeatureComment.objects.filter(feature__pk=pk)
    user_views = request.session.get('user_feature_views', [])

    # don't count views if the user is the author and don't let increment views by refreshing the page
    if feature.author_id != request.user.id and feature.id not in user_views:
        feature.views += 1
        feature.save()
        user_views.append(feature.id)
        request.session['user_feature_views'] = user_views
        request.session.modified = True

    return render(request, 'single.html', {'item': feature,
                                           'comments': comments,
                                           'archive_name': 'features',
                                           'body_class': 'single_posts features',
                                           'comments_form': comment_form})


@login_required()
def add(request):
    if request.method == "POST":
        form = FeatureForm(request.POST)
        if form.is_valid():
            feature = form.save(commit=False)
            feature.author = request.user
            feature.save()
            messages.success(request, "Feature has been created")
            return redirect('feature_single', feature.pk)
    form = FeatureForm()
    return render(request, 'add_edit.html', {'form': form, 'title': 'Add new feature'})


@login_required()
def edit(request, pk):
    feature = get_object_or_404(Features, pk=pk)
    if feature.author_id != request.user.id:
        messages.error(request, "You cannot edit someone feature")
        return redirect('feature_single', feature.pk)

    if request.method == "POST":
        form = FeatureForm(request.POST, instance=feature)

        if form.is_valid():
            feature = form.save(commit=False)
            feature.save()
            messages.success(request, "Feature has been edited")
            return redirect('feature_single', feature.pk)

    form = FeatureForm(instance=feature)
    return render(request, 'add_edit.html', {'form': form, 'title': 'Edit feature'})


@login_required()
def delete(request, pk):
    if request.method == "POST":
        feature = get_object_or_404(Features, pk=pk)
        current_user = request.user
        if feature.author_id != current_user.id:
            messages.error(request, "You cannot delete someone feature")
            return redirect(reverse('feature_archive'))
        feature.delete()
        return redirect(reverse('feature_archive'))
