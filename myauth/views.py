from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import RegistrationForm, LoginForm


# Create your views here.
def home(req):
    if 'next' in req.GET:
        messages.error(req, 'You must be logged in to view this page.')
    return render(req, 'index.html', {})


def login(req):
    if req.method == 'POST':
        form = LoginForm(data=req.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(req, user)
            req.session['id'] = user.id
            req.session['username'] = user.username
            return HttpResponseRedirect(reverse('myauth.home'))
        else:
            context = {'form': LoginForm(), 'messages': ['Invalid Credentials!', *form.errors['__all__']]}
            return render(req, 'myauth/login.html', context)

    context = {'form': LoginForm()}
    return render(req, 'myauth/login.html', context)


def register(req):
    if req.method == 'POST':
        form = RegistrationForm(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myauth.home'))
        else:
            context = {'form': RegistrationForm(), 'messages': ['Invalid Data!', *form.errors['__all__']]}
            return render(req, 'myauth/register.html', context)

    context = {'form': RegistrationForm()}
    return render(req, 'myauth/register.html', context)


def logout(req):
    auth_logout(req)
    req.session.clear()
    return HttpResponseRedirect(reverse('myauth.home'))
