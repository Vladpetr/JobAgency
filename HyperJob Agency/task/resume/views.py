from django.shortcuts import render, redirect
from django.views import View
from resume.models import Resume
from django.http import HttpResponseForbidden

# Create your views here.


class ResumeView(View):
    template_name = 'resume/resumePage.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'resumes': Resume.objects.all()})


class CreateResumeView(View):
    template_name = 'resume/createResume.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not request.user.is_staff:
                description = request.POST.get('description')
                Resume.objects.create(author=request.user, description=description)
                return redirect('/home')
        return HttpResponseForbidden(status=403)