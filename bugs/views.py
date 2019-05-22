from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Bugs, BugComment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BugForm, BugCommentForm


@login_required()
def archive(request):
    bugs = Bugs.objects.all()
    return render(request, 'archive.html', {'bugs': bugs})


@login_required()
def single(request, pk):
    return render(request, 'single.html')


@login_required()
def add_or_edit(request, pk=None):
    bug = get_object_or_404(Bugs, pk=pk) if pk else None
    return render(request, 'add_edit.html')


@login_required()
def vote(request, pk):
    # https://stackoverflow.com/questions/17114676/checking-if-an-item-is-contained-in-a-manytomanyfield-django
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
