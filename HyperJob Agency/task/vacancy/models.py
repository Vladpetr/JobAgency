from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Vacancy(models.Model):
    description = models.CharField(max_length=1024)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


'''Vacancy.objects.create(
    author=User.objects.create(username="Akuna Capital"),
    description="Quantitative Trader")
Vacancy.objects.create(
    author=User.objects.create(username="Cisco"),
    description="Software Engineer")
Vacancy.objects.create(
    author=User.objects.create(username="Citadel"),
    description="Infrastructure Operations Manager")
Vacancy.objects.create(
    author=User.objects.create(username="Credit Suisse"),
    description="Consultant")
Vacancy.objects.create(
    author=User.objects.create(username="Facebook"),
    description="Data analyst")
Vacancy.objects.create(
    author=User.objects.create(username="Google"),
    description="Backend Developer")
Vacancy.objects.create(
    author=User.objects.create(username="Tesla"),
    description="Program Manager")'''
