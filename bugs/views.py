from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Bugs, BugComment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BugForm, BugCommentForm


@login_required()
def archive(request):
    bugs = Bugs.objects.all().order_by('-published')
    return render(request, 'archive.html', {'bugs': bugs})


@login_required()
def single(request, pk):
    bug = get_object_or_404(Bugs, pk=pk)
    if request.method == "POST":

        form = BugCommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.bug = bug
            comment.author = request.user
            comment.save()
            messages.success(request, "Comment has been added")
            return redirect(reverse('bug_single', kwargs={'pk': pk}))

    comment_form = BugCommentForm()
    comments = BugComment.objects.filter(bug__pk=bug.pk)
    comments_total = len(comments)
    user_views = request.session.get('user_bug_views', [])

    # don't count views if the user is the author and don't let increment views by refreshing the page
    if bug.author_id != request.user.id and bug.id not in user_views:
        bug.views += 1
        bug.save()
        user_views.append(bug.id)
        request.session['user_bug_views'] = user_views
        request.session.modified = True

    return render(request, 'single.html', {'bug': bug,
                                           'comments': comments,
                                           'comments_total': comments_total,
                                           'comments_form': comment_form})


@login_required()
def add(request):
    if request.method == "POST":
        form = BugForm(request.POST)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.author = request.user
            bug.save()
            messages.success(request, "Bug has been created")
            return redirect('bug_single', bug.pk)
    form = BugForm()
    return render(request, 'add.html', {'form': form})


@login_required()
def edit(request, pk):
    bug = get_object_or_404(Bugs, pk=pk)
    if bug.author_id != request.user.id:
        messages.error(request, "You cannot edit someone bug")
        return redirect('bug_single', bug.pk)

    if request.method == "POST":
        form = BugForm(request.POST, instance=bug)

        if form.is_valid():
            bug = form.save(commit=False)
            bug.save()
            messages.success(request, "Bug has been edited")
            return redirect('bug_single', bug.pk)

    form = BugForm(instance=bug)
    return render(request, 'edit.html', {'form': form})


@login_required()
def vote(request, pk):
    if request.method == "POST":
        bug = get_object_or_404(Bugs, pk=pk)
        current_user = request.user
        # if current user is the author dont let vote
        if bug.author_id == current_user.id:
            messages.error(request, "You cannot vote for own bug")
            return redirect(reverse('bug_archive'))
        # assign Vote / Un vote action
        if bug.voted_by.filter(pk=current_user.id).exists():
            bug.voted_by.remove(current_user)
        else:
            bug.voted_by.add(current_user)
        bug.save()
    return redirect(reverse('bug_archive'))


@login_required()
def delete(request, pk):
    if request.method == "POST":
        bug = get_object_or_404(Bugs, pk=pk)
        current_user = request.user
        if bug.author_id != current_user.id:
            messages.error(request, "You cannot delete someone bug")
            return redirect(reverse('bug_archive'))
        bug.delete()
        return redirect(reverse('bug_archive'))
