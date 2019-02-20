""" View for django """
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from django.conf import settings


def login_view(request):
    """ show login page """
    return render(request, 'authentication/login.html')


def try_login(request):
    """ trying to login with the given username and password """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(reverse('authentication:authenticated_view'))
        # return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    return HttpResponse('Invalid login')


def register_view(request):
    """ show register page """
    return render(request, 'authentication/register.html')


def try_register(request):
    """ trying to register """
    pass


def logout_view(request):
    """ logout any authenticated user then show logout page """
    logout(request)
    return render(request, 'authentication/logout.html')


def authenticated_view(request):
    """ only authenticated user can access this page """
    if not request.user.is_authenticated:
        return render(request, 'authentication/login_error.html')

    return render(request, 'authentication/authenticated_view.html')


@login_required()
def authenticated_view_with_decorator(request):
    """ this is how to use decorators as middleware """
    return render(request, 'authentication/authenticated_view.html')
