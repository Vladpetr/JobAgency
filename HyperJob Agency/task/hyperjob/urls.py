"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from menu.views import MenuView, MySignupView, MyLoginView, PersonalProfileView
from vacancy.views import VacancyView, CreateVacancyView
from resume.views import ResumeView, CreateResumeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MenuView.as_view()),
    path('vacancies/', VacancyView.as_view()),
    path('resumes/', ResumeView.as_view()),
    re_path('signup/?', MySignupView.as_view()),
    re_path('login/?', MyLoginView.as_view()),
    re_path('home/?', PersonalProfileView.as_view()),
    path('resume/new', CreateResumeView.as_view()),
    path('vacancy/new', CreateVacancyView.as_view()),
]
