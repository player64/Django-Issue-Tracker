from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required


def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('login'))


def login(request):
    """If authenticated redirect to index"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    """A view that manages the login form"""
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(request.POST['email'],
                                     password=request.POST['password'])
            if user:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")

                if request.GET and request.GET['next'] != '':
                    return HttpResponseRedirect(request.GET['next'])
                else:
                    return redirect(reverse('index'))
            else:
                login_form.add_error(None, 'Entered credentials seems to be invalid')
    else:
        login_form = UserLoginForm()

    return render(request, 'login.html', {'login_form': login_form, 'next': request.GET.get('next', '')})


@login_required
def profile(request):
    """A view that displays the profile page of a logged in user"""
    return render(request, 'profile.html')


def register(request):
    """If authenticated redirect to index"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    """A view that manages the registration form"""
    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, 'You have successfully registered')
                return redirect(reverse('index'))

            else:
                messages.error(request, 'Unable to log you in at this time!')
    else:
        registration_form = UserRegistrationForm()

    return render(request, 'register.html', {'registration_form': registration_form})
