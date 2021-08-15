from django.shortcuts import render, redirect
from django.views import View

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

# Create your views here.
menu = {'Login page': '/login', 'Sign Up page': '/signup', 'Vacancy list': '/vacancies', 'Resume list': '/resumes',
        'Personal profile': '/home'}


class MenuView(View):
    template_name = 'menu/menu.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'menu': menu})


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'menu/signup.html'


class MyLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = 'menu/login.html'


class PersonalProfileView(View):
    def get(self, request, *args, **kwargs):

        if request.user.is_staff:
            return redirect('/vacancy/new')
        else:
            return redirect('/resume/new')
        
