from django.shortcuts import render, redirect
from django.views import View
from vacancy.models import Vacancy
from django.http import HttpResponseForbidden

# Create your views here.


class VacancyView(View):
    template_name = 'vacancy/vacancyPage.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'vacancies': Vacancy.objects.all()})


class CreateVacancyView(View):
    template_name = 'vacancy/createVacancy.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                description = request.POST.get('description')
                Vacancy.objects.create(author=request.user, description=description)
                return redirect('/home')
        return HttpResponseForbidden(status=403)