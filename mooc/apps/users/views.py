from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

from apps.users.forms import LoginForm

# Create your views here.


# Logout view
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        # Defin logout in urls.py
        logout(request)
        return render(request, 'index.html')



# Login view
class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):

        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            # user_name = request.POST.get('username', '')
            # password = request.POST.get('password', '')

            user_name = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']


            # Validation (Django built-in authenticate class)

            # Validate data
            # Backend takes care of validation
            # Frontend validation is vulnerable
            if not user_name:
                return render(request, 'login.html', {'msg': 'Please enter username'})

            if not password:
                return render(request, 'login.html', {'msg': 'Please enter password'})

            user = authenticate(username=user_name, password=password)
            if user is not None:
                # User Django built-in login method
                login(request, user)
                # return to home page
                return HttpResponseRedirect(reverse('index'))

            else:
                return render(request, 'login.html', {'msg': 'Username or password error!'})

        else:
            return render(request, 'login.html', {'msg': 'Username or password error!'})


